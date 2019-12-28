from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from app.models import NewsItem


class HomeView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data()
        context['news'] = NewsItem.objects.filter(published=True).order_by('-created')[:3]
        return context


class NewsListView(ListView):

    template_name = "news.html"
    queryset = NewsItem.objects.filter(published=True).order_by('-created')