from django.urls import path
from . import views

app_name = 'szkola_jazdy'

urlpatterns = [
    path('', views.home, name='home'),
]
