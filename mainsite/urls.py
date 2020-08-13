from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.displayPayments, name='dash_home'),
]
