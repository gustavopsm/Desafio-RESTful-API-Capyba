from django.test import TestCase
from django.urls import reverse, resolve
from ..views import Inicio, Menu

class UrlsTestCase(TestCase):

    def test_menu_url(self):
        url = reverse('menu')

        self._getAssertEqualityFunc(resolve(url).func, Menu.as_view())
    
    def test_inicio_url(self):
        url = reverse('inicio')

        self._getAssertEqualityFunc(resolve(url).func, Inicio.as_view())
    