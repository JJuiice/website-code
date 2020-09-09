from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('LICENSE/', views.home_license, name='LICENSE')
]
