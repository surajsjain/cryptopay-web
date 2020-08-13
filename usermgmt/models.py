from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    singtype = models.CharField(max_length=6, default='payer')
    ardor_public_key = models.CharField(max_length=100, blank=True, default='')
    ardor_acc_num = models.CharField(max_length=26, blank=True, default='')

class APIAccessKey(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    key = models.CharField(max_length=30)
