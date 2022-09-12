from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class loginViewTestCase(TestCase):

    def test_status_get_cadastro(self):
        response = self.client.get(reverse('cadastro'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/cadastro.html')

    def test_status_post_cadastro_success(self):
        response = self.client.post(reverse('cadastro'), {
            'username': 'something',
            'email': 'something@something.com',
            'password': 'something',
            'foto_perfil': ''})

        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.count(), 1)
        self.assertRedirects(response, '/usuarios/login', status_code=302, 
        target_status_code=301, fetch_redirect_response=True)
    
    def test_status_post_cadastro_fail(self):
        response = self.client.post(reverse('cadastro'), {
            'username': 'something',
            'email': 'somethething.com',
            'password': 1,
            'foto_perfil': ''})

        self.assertEquals(response.status_code, 302)
        self.assertEquals(User.objects.count(), 0)
        self.assertRedirects(response, '/usuarios/login', status_code=302, 
        target_status_code=301, fetch_redirect_response=True)
    
class LoginViewTestCase(TestCase):

    def test_status_get_login(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/login.html')

    def test_status_post_login_success(self):
        User.objects.create(username='something', email='something@something.com', password='d*rt&yhr4567bu656tyu')
        response = self.client.post(reverse('login'), {
            'username': 'something',
            'password': 'd*rt&yhr4567bu656tyu'
            })
        
        self.assertRedirects(response, '/menu', status_code=302, 
        target_status_code=301, fetch_redirect_response=True)
    
    def test_status_post_login_fail(self):
        User.objects.create(username='something', email='something@something.com', password='something')
        response = self.client.post(reverse('login'), {
            'username': 'something',
            'password': 'wrong'
            })

        self.assertRedirects(response, '/usuarios/cadastro', status_code=302, 
        target_status_code=301, fetch_redirect_response=True)


class LogoutViewTestCase(TestCase):

    def test_status_get_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, '/', status_code=302, 
        target_status_code=200, fetch_redirect_response=True)


class PerfilViewTestCase(TestCase):

    def test_status_get_perfil(self):
        response = self.client.get(reverse('perfil'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/perfil.html')
    
class PoliticasViewTestCase(TestCase):

    def test_status_get_politicas(self):
        response = self.client.get(reverse('politicas'))
        self.assertEquals(response.status_code, 200)

class VerificaremailViewTestCase(TestCase):

    def test_status_get_verificaremail(self):
        response = self.client.get(reverse('verificaremail'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/verificaremail.html')

class MudarsenhaViewTestCase(TestCase):

    def test_status_get_mudarsenha(self):
        response = self.client.get(reverse('mudarsenha'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'usuarios/mudarsenha.html')