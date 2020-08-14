from django.urls import path, include

from . import rest_apis

urlpatterns = [
    path('register/', rest_apis.RegisterTransaction.as_view(), name='reg_transaction'),
    path('confirm/', rest_apis.ConfirmTransaction.as_view(), name='conf_transaction'),
]
