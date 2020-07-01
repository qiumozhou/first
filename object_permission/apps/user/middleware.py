#-*-coding:utf-8-*-
#-*-coding:utf-8-*-
from django.utils.deprecation import MiddlewareMixin
class NotUseCsrfTokenMiddlewareMixin(MiddlewareMixin):
    def process_request(self,request):
        setattr(request, '_dont_enforce_csrf_checks', True)
