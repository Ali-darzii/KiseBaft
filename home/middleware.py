import geoip2.database
from django.conf import settings
from django.shortcuts import redirect

class LanguageRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.reader = geoip2.database.Reader(settings.GEOIP_PATH)

    def __call__(self, request):
        if not request.path.startswith(('/fa', '/ar', '/en')):
            ip = self.get_client_ip(request)
            country = self.get_country(ip)
            
            if country in ['IR']:  # Iran
                return redirect('/fa/')
            elif country in ['AE', 'SA', 'EG']:  # Arabic-speaking countries
                return redirect('/ar/')
            else:  # Default to English
                return redirect('/en/')
        
        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')

    def get_country(self, ip):
        try:
            response = self.reader.country(ip)
            return response.country.iso_code
        except Exception:
            return None
