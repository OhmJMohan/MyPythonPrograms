"""myDailyAccountEntry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.mdae_homePage),
    path('add_category/', views.add_category),
    path('add_category/addcategory/', views.addcategory),
    path('category_view/', views.category_view),
    path('deleteCategory/<int:id>', views.deleteCategory),
    path('delete/<int:id>', views.delete_view),
    path('update_category/<int:id>', views.update_category),
    path('update_category/updaterecord/<int:id>', views.updaterecord),
    path('add/', views.add),
    path('add/addAccountEntry/', views.addAccountEntry),
    path('sample/', views.sample),
]
