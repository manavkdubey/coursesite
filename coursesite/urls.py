"""
URL configuration for coursesite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from courses import views
from courses.views import buy_course
from users.views import account,register
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.home,name='home'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('register/', register, name='register'),
    path('account/', account, name='account'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('buy_course/<int:course_id>/', buy_course, name='buy_course'),
    path('account/', account, name='account'),
    path('add_course/', views.add_course, name='add_course'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
