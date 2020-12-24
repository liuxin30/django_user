from django.urls import path

from . import views

app_name = 'note'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/', views.index, name='edit'),
    path('list/', views.index, name='list'),
    path('detail/', views.index, name='detail'),
]