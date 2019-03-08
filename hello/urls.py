from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.base,name='hello-base'),
    path('home', views.home, name='hello-home'),
    path('about', views.about, name='hello-about'),
    path('contact', views.contact, name='hello-contact')
]



