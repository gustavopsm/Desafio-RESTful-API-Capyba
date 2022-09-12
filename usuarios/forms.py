from django import forms

class ProfileCreateForm(forms.Form):
    username = forms.CharField(help_text="")
    email = forms.EmailField(help_text="")
    foto_perfil = forms.FileField(help_text="", required=False)
    password = forms.CharField(help_text="", widget=forms.PasswordInput())

class ProfileLoginForm(forms.Form):
    username = forms.CharField(help_text="")
    password = forms.CharField(help_text="", widget=forms.PasswordInput())

class ProfileEditForm(forms.Form):
    username = forms.CharField(help_text="")
    email = forms.EmailField(help_text="")
    foto_perfil = forms.FileField(help_text="", required=False)

class PasswordEditForm(forms.Form):
    novasenha = forms.CharField(help_text="")
    password = forms.CharField(help_text="", widget=forms.PasswordInput())
