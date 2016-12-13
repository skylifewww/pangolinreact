import json

from django.core.urlresolvers import reverse
from django.test import SimpleTestCase
from django.test.utils import override_settings


@override_settings(CELERY_ALWAYS_EAGER=True, BROKER_BACKEND='memory')
class TestCase(SimpleTestCase):
    fixtures = []

    def reverse(self, *args, **kwargs):
        return reverse(*args, **kwargs)

    def get_ajax(self, *args, **kwargs):
        kwargs.update({'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        return self.client.get(*args, **kwargs)

    def post_ajax(self, *args, **kwargs):
        kwargs.update({'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'})
        return self.client.post(*args, **kwargs)

    def json_response(self, response):
        return json.loads(response.content.decode('utf-8'))
