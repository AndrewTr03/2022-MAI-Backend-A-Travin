"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from armen_app import views

from armen_app.views import ColorViewSet, BootViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("django/boots", BootViewSet, basename="boots")
router.register("boots", BootViewSet, basename="boots")
router.register("django/colors", ColorViewSet, basename="colors")
router.register("colors", ColorViewSet, basename="colors")

urlpatterns = [
    path('', views.index, name='home'),
    path('django/', views.index, name='home'),

    path('admin/', admin.site.urls),
]

urlpatterns += router.urls
