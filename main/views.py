from string import Template

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories

class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Home - Главная"
        context['content'] = "Магазин мебели Home"
        return context

class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Home - Главная"
        context['content'] = "Магазин мебели Home"
        context['text_on_page'] = "Классный магазин"
        return context

# Create your views here.
# def index(request):
    
#     context = {
#         "title": "Home - Главная",
#         "content": "Магазин мебели Home",
#     }
#     return render(request, "main/index.html", context)


# def about(request):
#     context = {
#         "title": "Home - О нас",
#         "content": "О нас",
#         "text_on_page": "hjhajhjkha",
#     }
#     return render(request, "main/about.html", context)
