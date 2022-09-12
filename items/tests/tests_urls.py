from django.test import TestCase
from django.urls import reverse, resolve
from ..views import Items

class UrlsTestCase(TestCase):

    def test_items_url(self):
        url = reverse('menu')

        self._getAssertEqualityFunc(resolve(url).func, Items.as_view())