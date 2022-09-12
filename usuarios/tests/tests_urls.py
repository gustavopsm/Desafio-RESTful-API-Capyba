from django.test import TestCase
from django.urls import reverse, resolve
from ..views import cadastro, login, perfil, logout, politicas, verificaremail, mudarsenha

class UrlsTestCase(TestCase):

    def test_cadastro_url(self):
        url = reverse('cadastro')

        self.assertEquals(resolve(url).func, cadastro)
    
    def test_login_url(self):
        url = reverse('login')

        self.assertEquals(resolve(url).func, login)
    
    def test_perfil_url(self):
        url = reverse('perfil')

        self.assertEquals(resolve(url).func, perfil)
    
    def test_logout_url(self):
        url = reverse('logout')

        self.assertEquals(resolve(url).func, logout)
    
    def test_politicas_url(self):
        url = reverse('politicas')

        self.assertEquals(resolve(url).func, politicas)
    
    def test_verificaremail_url(self):
        url = reverse('verificaremail')

        self.assertEquals(resolve(url).func, verificaremail)
    
    def test_mudarsenha_url(self):
        url = reverse('mudarsenha')

        self.assertEquals(resolve(url).func, mudarsenha)

    