from django.db import models
from django.contrib.auth.models import User

from usermgmt.models import APIAccessKey

# Create your models here.
class Transaction(models.Model):
    chain = models.IntegerField(default=1)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    apikey = models.ForeignKey(APIAccessKey, on_delete=models.CASCADE, default=None)
    datetime = models.DateTimeField(auto_now_add=True)
    checkout_code = models.CharField(max_length=100, blank=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer', default=None)
    completed = models.BooleanField(default=False)
    amount = models.FloatField()

    transaction_res = models.CharField(max_length=1000, default='')
