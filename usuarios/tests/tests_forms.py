from django.test import TestCase
from ..forms import ProfileCreateForm, PasswordEditForm, ProfileEditForm, ProfileLoginForm

class ProfileCreateFormTestCase(TestCase):

    def test_profile_create_form_valid_data(self):
        form = ProfileCreateForm(data={
            'username': 'something',
            'email': 'something@something.com',
            'password': 'something',
            'foto_perfil': ''})
        
        self.assertTrue(form.is_valid())
    
    def test_profile_create_form_no_data(self):
        form = ProfileCreateForm(data={})
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)


class ProfileLoginFormTestCase(TestCase):

    def test_profile_login_form_valid_data(self):
        form = ProfileLoginForm(data={
            'username': 'something',
            'password': 'something',
            })
        
        self.assertTrue(form.is_valid())
    
    def test_profile_login_form_no_data(self):
        form = ProfileLoginForm(data={})
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)


class ProfileEditFormTestCase(TestCase):

    def test_profile_edit_form_valid_data(self):
        form = ProfileEditForm(data={
            'username': 'something',
            'email': 'something@something.com',
            'password': 'something',
            'foto_perfil': ''})
        
        self.assertTrue(form.is_valid())
    
    def test_profile_edit_form_no_data(self):
        form = ProfileEditForm(data={})
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)


class PasswordEditFormTestCase(TestCase):

    def test_password_edit_form_valid_data(self):
        form = PasswordEditForm(data={
            'novasenha': 'something',
            'password': 'something'})
        
        self.assertTrue(form.is_valid())
    
    def test_password_edit_form_no_data(self):
        form = PasswordEditForm(data={})
        
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)