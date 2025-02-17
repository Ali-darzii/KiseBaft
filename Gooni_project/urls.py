"""
URL configuration for Gooni_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from home import views as home
from about_us import views as about_us
from contact_us import views as contact_us
from products import views as products
from django.conf.urls.static import static
from django.conf import settings
# from django.utils.translation import
urlpatterns = [
    path('products/load-more/', products.load_more_product),
    path('products/filter/', products.filter_product),
    path('products/search/', home.search_page, name='search_page'),
    path('admin/', admin.site.urls),

]
urlpatterns += i18n_patterns(
    path('', home.IndexPageView.as_view(), name='index_page'),
    path('about-us/', about_us.AboutUsView.as_view(), name='about_us_page'),
    path('contact-us/', contact_us.ContactUsView.as_view(), name='contact_us_page'),
    path('products/', products.product_list, name='product_list_page'),
    path('products/<slug:slug>', products.ProductDetail.as_view(), name='product_detail_page'),


    prefix_default_language=True
)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
