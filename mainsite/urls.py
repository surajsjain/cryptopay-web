from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.displayPayments, name='dash_home'),
    path('apikeys/', views.displayAPIKeys, name='api_keys'),
    path('apikeys/new/', views.newAPIKey, name='new_key'),
    path('apikeys/delete/<int:key_id>/', views.deleteAPIKey, name='delete_key'),
]
