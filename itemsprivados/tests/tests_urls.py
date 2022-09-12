from django.test import TestCase
from django.urls import reverse, resolve
from ..views import ItemsPrivados

class UrlsTestCase(TestCase):

    def test_itemsprivados_url(self):
        url = reverse('menu')

        self._getAssertEqualityFunc(resolve(url).func, ItemsPrivados.as_view())