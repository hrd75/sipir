from django.urls import path
from . import views

app_name = 'mainMenu'

urlpatterns = [
    #path('buat/', views.index, name='index'),
    path('', views.index, name='index'),
]