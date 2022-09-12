from django.http import HttpResponseRedirect, FileResponse
from django.shortcuts import render
from django.contrib.auth import models, hashers, authenticate, login as login_django, logout as logout_django
from .forms import ProfileCreateForm, ProfileEditForm, PasswordEditForm, ProfileLoginForm
from .classes import Email


def cadastro(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
        context = {
            'form': form
        }
        return render(request, 'usuarios/cadastro.html', context=context)
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            foto_perfil = form.cleaned_data['foto_perfil']
            user = models.User.objects.create(username=username, email=email, password=password)
            user.profile.foto_perfil = foto_perfil
            user.profile.save(update_fields=['foto_perfil'])
        else:
            print(form.errors)
        return HttpResponseRedirect('/usuarios/login')

def login(request):
    if request.method == 'GET':
        form = ProfileLoginForm()
        context = {
            'form': form
        }
        return render(request, 'usuarios/login.html', context=context)
    else:
        form = ProfileLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login_django(request, user)
                return HttpResponseRedirect('/menu')
            else:
                return HttpResponseRedirect('/usuarios/cadastro')
        else:
            print(form.errors)
            return HttpResponseRedirect('/')

def logout(request):
    logout_django(request)
    return HttpResponseRedirect('../../../')

def perfil(request):
    if request.method == 'GET':
        form = ProfileEditForm()
        context = {
            'form': form
        }
        return render(request, 'usuarios/perfil.html', context=context)
    else:
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            foto_perfil = form.cleaned_data['foto_perfil']

            user = models.User.objects.get(id=request.user.id)

            user.username = username
            user.email = email
            user.profile.foto_perfil = foto_perfil
            user.save(update_fields=['username', 'email'])
            user.profile.save(update_fields=['foto_perfil'])
        else:
            print(form.errors)
        return HttpResponseRedirect('/usuarios/login')

def politicas(request):
    return FileResponse(open('static/politicas.pdf', 'rb'), content_type='application/pdf')

mail = Email()

def verificaremail(request):
    if request.method == "GET":
        context = {
        'user': request.user
        }
        mail.mudarCodigo()
        mail.mandarEmail(request.user.email)
        return render(request, 'usuarios/verificaremail.html', context=context)
    else:
        codigo_digitado = str(request.POST.get('codigo_digitado'))
        if codigo_digitado == mail.codigo:
            user = models.User.objects.get(id=request.user.id)
            user.profile.verificado = True
            user.profile.save(update_fields=['verificado'])

        return HttpResponseRedirect('/usuarios/perfil')

def mudarsenha(request):
    if request.method == 'GET':
        form = PasswordEditForm()
        context = {
            'form': form
        }
        return render(request, 'usuarios/mudarsenha.html', context=context)
    else:
        form = PasswordEditForm(request.POST)
        if form.is_valid():
            novasenha = form.cleaned_data['novasenha']
            password = form.cleaned_data['password']
            print(novasenha, password)
            user = models.User.objects.get(id=request.user.id)
            print(user.password)
            if hashers.check_password(password, user.password):
                user.set_password(novasenha)
                user.save()
                print('entrou')

        else:
            print(form.errors)
        return HttpResponseRedirect('/usuarios/perfil')