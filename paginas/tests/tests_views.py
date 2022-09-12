from django.test import TestCase
from django.urls import reverse

class InicioViewTestCase(TestCase):

    def test_status_get_inicio(self):
        response = self.client.get(reverse('inicio'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'paginas/inicio.html')

class MenuViewTestCase(TestCase):

    def test_status_get_menu(self):
        response = self.client.get(reverse('menu'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'paginas/menu.html')