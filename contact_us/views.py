from django.views.generic import TemplateView
from contact_us.models import ContactUsBox, ContactUs


class ContactUsView(TemplateView):
    template_name = 'contact_us/contact_us_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["boxes"] = ContactUsBox.objects.filter(is_active=True)
        context["contact_us"] = ContactUs.objects.filter(is_active=True).first()
        return context
