from django.db.models import Count
from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import TemplateView

from home.models import Slider, HomeBox
from products.models import Product, ProductType, SimpleBag, StockBag


# Create your views here.


class IndexPageView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["slider"] = Slider.objects.filter(is_active=True).first()
        context["boxes"] = HomeBox.objects.filter(is_active=True)
        context["new_products"] = Product.objects.filter(is_delete=False, is_active=True, inventory=True).order_by(
            'id')[:5]
        context["product_10"] = Product.objects.filter(is_active=True, is_delete=False, inventory=True).order_by(
            '-title_en')
        context["products_types"] = ProductType.objects.filter(is_active=True).all()
        context["simple_bags"] = SimpleBag.objects.filter(is_active=True).all()
        context["stock_bags"] = StockBag.objects.filter(is_active=True).all()

        return context


def search_page(request: HttpRequest):
    q = request.GET.get('q')
    if q == '' or q is None:
        return JsonResponse({
            "status": "empty"
        })
    products: Product = Product.objects.filter(is_delete=False, is_active=True, title__icontains=q)
    count = False
    if products.count() <= 0:
        count = True
    return JsonResponse({
        "status": "success",
        "data": render_to_string("home/search.html", {'products': products, "q": q, 'count': count})
    })


def header_component(request: HttpRequest):
    return render(request, 'shared/header_component.html')


def footer_component(request: HttpRequest):
    return render(request, 'shared/footer_component.html')
