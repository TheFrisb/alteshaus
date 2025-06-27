from django.shortcuts import render
from django.views.generic import TemplateView, DetailView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'shop/home.html'


class AboutView(TemplateView):
    template_name = 'shop/about.html'


class ShopView(DetailView):
    template_name = 'shop/shop.html'