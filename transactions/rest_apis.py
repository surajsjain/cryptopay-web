from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView

from . models import *
from usermgmt.models import APIAccessKey

class RegisterTransaction(APIView):

    def get(self, request, format=None):
        return Response({"Message": "Try the POST request, GET request can\'t be done on this API"})


    def post(self, request, format=None):
        data = request.data
        api_key = data['key']
        try:
            try:
                accessKey = APIAccessKey.objects.get(key = api_key)
            except:
                return Response({"transaction_status": "invalid key error"})
            seller = accessKey.user

            tr = Transaction()
            tr.seller = seller
            tr.apikey = accessKey
            try:
                tr.customer = User.objects.get(email=data['customer_email'])
            except:
                return Response({"transaction_status": "customer not found"})
            tr.amount = data['amount']
            tr.save()

            tr.checkout_code = ("".join(tr.apikey.name.split(" ")))+'-'+str(tr.id)
            tr.save()

            return Response({"transaction_status": "registered", "id": tr.id, "checkout_code": tr.checkout_code})

        except:
            return Response({"transaction_status": "error"})
