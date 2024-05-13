from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^get_sentiment/$', views.get_sentiment, name='get_sentiment'),
]