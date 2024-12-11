from django.urls import path
from . import views
from django.urls import reverse


app_name = 'szkola_jazdy'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('about_us/', views.about_us, name='about_us'),
]
