from django.views.generic import TemplateView

class Inicio(TemplateView):
    template_name = "paginas/inicio.html"

class Menu(TemplateView):
    template_name = "paginas/menu.html"