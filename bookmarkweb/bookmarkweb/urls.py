"""bookmarkweb URL Configuration

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
from bookmarkdatabase import views as bm_views
from django.contrib.auth import views as auth_views
from user import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/<str:un>', bm_views.bookmark_list),
    path('add/', bm_views.add),
    path('add/addlink/<str:un>', bm_views.addlink),
    path('deleteLink/<str:un>', bm_views.deleteLink),
    path('delete/<int:id>/<str:un>', bm_views.delete_view),
    path('updateLink/<str:un>', bm_views.update_page),
    path('update/<int:id>', bm_views.update),
    path('update/updaterecord/<int:id>/<str:un>', bm_views.updaterecord),
    path('MPBW', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
]
