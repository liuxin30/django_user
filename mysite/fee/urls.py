from django.urls import path

from . import views

app_name = 'fee'
urlpatterns = [
    path('', views.index, name='index'),
    path('show/', views.index, name='show'),
]