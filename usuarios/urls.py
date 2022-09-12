from django.urls import path
from .views import cadastro, login, logout, perfil, politicas, mudarsenha, verificaremail

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('cadastro/', cadastro, name='cadastro'),
    path('perfil/', perfil, name='perfil'),
    path('politicas/', politicas, name='politicas'),
    path('verificaremail/', verificaremail, name='verificaremail'),
    path('mudarsenha/', mudarsenha, name='mudarsenha')

]