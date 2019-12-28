from django.contrib.flatpages import views
from django.urls import path, include

from app.views import HomeView, NewsListView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('news/', NewsListView.as_view(), name='news'),
    path('<path:url>', views.flatpage),
]