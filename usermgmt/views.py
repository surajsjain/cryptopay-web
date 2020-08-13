from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

from .models import *

# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, 'pages/login.html')
    else:
        data = request.POST
        email = data['email']
        password = data['password']

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):

                usr_det = UserDetails.objects.get(user = user)
                if(usr_det.singtype == 'seller'):
                    auth.login(request, user)
                    return redirect('dash_home')
                else:
                    return redirect('phonedownload')

            else:
                return redirect('login')

        except:
            return redirect('login')
def signup(request):

    if request.method == 'GET':
        return render(request, 'pages/signup.html')

    else:
        inData = request.POST

        user = User.objects.create_user(username=inData['username'], first_name = inData['firstname'], last_name = inData['lastname'], email = inData['email'], password = inData['password'])
        user.save()

        usr_det = UserDetails()
        usr_det.user = user
        usr_det.singtype = inData['signtype']
        usr_det.ardor_public_key = inData['ardor_public_key']

        if(inData['signtype'] == 'seller'):
            usr_det.ardor_acc_num = inData['ardor_acc']

        usr_det.save()

        if(inData['signtype'] == 'seller'):
            auth.login(request, user)
            return redirect('dash_home')

        else:
            return redirect('phonedownload')

def phoneDownload(request):
    return render(request, 'pages/phoneLogIn.html')

def logout(request):
    # if request.method == 'POST':
    auth.logout(request)

    return redirect('login')
