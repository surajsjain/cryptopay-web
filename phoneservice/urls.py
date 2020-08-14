from django.urls import path, include
from . import restAPIs
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('login/', restAPIs.Login.as_view(), name='rest_login'),
    path('logout/', restAPIs.Logout.as_view(), name='rest_logout'),
]
