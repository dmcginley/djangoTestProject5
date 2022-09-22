from django.urls import path
from xml.etree.ElementInclude import include

from . import views

urlpatterns = [
    path('', views.home, name='shop-home'),
]
