
from django.contrib import admin
from django.urls import path
from.import views
urlpatterns = [
    path('', views.home, name='home'),
    path('home.html',views.home,name="home"),
    path('adoption.html',views.adoption,name="adoption"),
    path('advice.html',views.advice,name="advice"),
    path('pets.html',views.pets,name="pets"),
    path('shop.html',views.shop,name="shop"),
    path('login.html',views.login,name="login"),
]
