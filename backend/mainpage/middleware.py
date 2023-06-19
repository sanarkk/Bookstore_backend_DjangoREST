from django.utils import translation
from django.utils.deprecation import MiddlewareMixin


class CustomLocaleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            if request.user.is_authenticated:
                translation.activate(request.user.profile.language)
                request.LANGUAGE_CODE = request.user.profile.language
        except:
            request.LANGUAGE_CODE = "en"
