from django.views.generic import TemplateView
from about_us.models import AboutUs


# Create your views here.


class AboutUsView(TemplateView):
    template_name = 'about_us/about_us_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['about_us'] = AboutUs.objects.filter(is_active=True).first()
        return context
