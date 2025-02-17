from django.db.models import Count
from django.http import HttpRequest, JsonResponse, Http404
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import DetailView
from utils.http_service import get_client_ip
from django.utils.translation import get_language_from_request
from products.models import Product, ProductGallery, ProductVisit, ProductType, SimpleBag, StockBag


# Create your views here.

def product_list(request: HttpRequest):
    raise Http404
    products = Product.objects.filter(is_active=True, is_delete=False).order_by('id')[:1]
    context = {
        'products': products,
        'product_count': products.count(),
        'products_types': ProductType.objects.filter(is_active=True).all(),
        'simple_bags': SimpleBag.objects.filter(is_active=True).all(),
        'stock_bags': StockBag.objects.filter(is_active=True).all(),
    }
    return render(request, 'products/product_list_template.html', context)


# todo:don't forget [:5] to [:20]
# todo:test load more
def load_more_product(request: HttpRequest):
    total_items = int(request.GET.get('lengths'))
    state = request.GET.get('state')
    order = request.GET.get('sort')
    cat_id = request.GET.get('value')
    limit = 1

    if state == '':
        products = Product.objects.filter(is_active=True, is_delete=False).distinct()
    elif state == 'productType':
        products = Product.objects.filter(is_active=True, is_delete=False, product_type_id=int(cat_id)).distinct()

    elif state == 'simpleBag':
        products = Product.objects.filter(is_active=True, is_delete=False, simple_bag_id=int(cat_id)).distinct()

    elif state == 'stockBag':
        products = Product.objects.filter(is_active=True, is_delete=False, stock_bag_id=int(cat_id)).distinct()

    else:
        products = Product.objects.all()

    if order == 'id':
        products = products.order_by('-id').distinct()[total_items:total_items + limit]
    else:
        products = products.annotate(visit_count=Count('productvisit')).order_by('-visit_count').distinct()[
                   total_items:total_items + limit]

    if products.count() <= 0:
        return JsonResponse({'status': 'failed'})
    return JsonResponse({
        'status': 'success',
        'data': render_to_string('product_ajax/ajax_filter.html', context={'products': products,
                                                                           'product_count': products.count()})
    })


# todo:don't forget [:5] to [:20]

def filter_product(request: HttpRequest):
    state = request.GET.get('state')
    cat_id = request.GET.get('value')
    order = request.GET.get('sort')
    if int(cat_id) != 0:

        if state == 'productType':
            products = Product.objects.filter(is_active=True, is_delete=False, product_type_id=int(cat_id)).distinct()

        elif state == 'simpleBag':
            products = Product.objects.filter(is_active=True, is_delete=False, simple_bag_id=int(cat_id)).distinct()

        elif state == 'stockBag':
            products = Product.objects.filter(is_active=True, is_delete=False, stock_bag_id=int(cat_id)).distinct()

        else:
            products = Product.objects.all().distinct()
    else:
        products = Product.objects.all().distinct()

    if order == 'id':
        products = products.order_by('-id').distinct()[:5]
    else:
        products = products.annotate(visit_count=Count('productvisit')).order_by('-visit_count').distinct()[:5]
    return JsonResponse({
        'status': 'success',
        'data': render_to_string('product_ajax/ajax_filter.html',
                                 context={'products': products}),
    })


class ProductDetail(DetailView):
    model = Product
    template_name = 'products/product_detail_template.html'

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(is_delete=False, is_active=True)
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        product: Product = kwargs.get('object')

        context['product_gallery_group'] = ProductGallery.objects.filter(product_id=self.object.id).all()
        # visit analyze
        user_ip = get_client_ip(self.request)
        has_been_visited = ProductVisit.objects.filter(ip__iexact=user_ip, product_id=self.object.id).exists()
        if not has_been_visited:
            ProductVisit.objects.create(ip=user_ip, product_id=self.object.id)

        context['related_products'] = Product.objects.filter(is_delete=False, is_active=True).order_by('?').exclude(id=self.object.id)[:5]
        return context

        # context['related'] = True
        # if product.product_type is not None:
        #
        #     context['related_products'] = Product.objects.filter(is_delete=False, is_active=True, inventory=True,
        #                                                          product_type_id=product.product_type.id).exclude(
        #         pk=product.id)[:5]
        # elif product.simple_bag is not None:
        #     context['related_products'] = Product.objects.filter(is_delete=False, is_active=True, inventory=True,
        #                                                          simple_bag_id=product.simple_bag.id).exclude(
        #         pk=product.id)[:5]
        # elif product.stock_bag is not None:
        #     context['related_products'] = Product.objects.filter(is_delete=False, is_active=True, inventory=True,
        #                                                          stock_bag_id=product.stock_bag.id).exclude(
        #         pk=product.id)[:5]
        #
        # else:
        #     context['related'] = False