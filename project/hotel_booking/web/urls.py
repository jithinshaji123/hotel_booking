from django.urls import path
from .import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
        path('signup/',views.register),
        path('login/', views.login0),
        path('webpage/', views.webpage),
        path('logout/',views.LogoutPage,name='logout'),
        path('book-now/', views.book_now, name='book_now'),
       

    

]