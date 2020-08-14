from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .custom_authenticators import CsrfExemptSessionAuthentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken.models import Token

from django.contrib.auth.models import User
from django.contrib import messages, auth

class Login(APIView):
    # authentication_classes = [CsrfExemptSessionAuthentication]
    permission_classes = [AllowAny]


    def get(self, request, format=None):
        return Response({"auth_status": False})

    def post(self, request, format=None):
        data = request.data

        email = data['email']
        password = data['password']

        try:
            user = User.objects.get(email=email)
            # print(user.password)
            if user.check_password(password):
                print('User authenticated')
                auth.login(request, user)
                print('User Logged in')
                token, _ = Token.objects.get_or_create(user=user)
                return Response({"auth_status": True, "auth_token": token.key})
            else:
                print('User not authenticated')
                return Response({"auth_status": False})
        except:
            return Response({"auth_status": False})

class Logout(APIView):
    def get(self, request, format=None):
        pass

    def get(self, request, format=None):
        pass
