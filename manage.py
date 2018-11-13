#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jysAdmin.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)

    from django.http import HttpResponseNotAllowed
import logging
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from kpw.site_manager import *
from kpw.user_manager import *

logger = logging.getLogger('django.request')


class KPWView(object):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

    def __new__(cls, request, *args, **kwargs):
        return super(KPWView, cls).__new__(cls)(request, *args, **kwargs)

    @method_decorator(login_required)
    def __call__(self, request, *args, **kwargs):
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed

        before_handler = getattr(self, 'before', None)
        before_handler(request, *args, **kwargs) if before_handler else None

        return handler(request, *args, **kwargs)

    def http_method_not_allowed(self, request, *args, **kwargs):
        logger.warning(
            'Method Not Allowed (%s): %s', request.method, request.path,
            extra={'status_code': 405, 'request': request}
        )
        return HttpResponseNotAllowed(self._allowed_methods())

    def _allowed_methods(self):
        return [m.upper() for m in self.http_method_names if hasattr(self, m)]


class KPWDashboardView(KPWView):
    def __new__(cls, request, *args, **kwargs):
        return super(KPWDashboardView, cls).__new__(cls)(request, *args, **kwargs)

    @method_decorator(login_required)
    def __call__(self, request, *args, **kwargs):
        if request.method.lower() == 'get':
            self.context = get_site_notice()
            self.context.update(get_user_interest_product_context(request.user))
            selected_product = get_user_selected_product(request.user)
            self.context.update({'selected_product': selected_product})
        return super().__call__(request, *args, **kwargs)
