from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth


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
                auth.login(request, user)
                # TODO: Redirect to the app download screen if the user is not a seller
                return redirect('dash_home')
            else:
                return redirect('login')

        except:
            return redirect('login')
def signup(request):
    return render(request, 'pages/signup.html')

def phoneDownload(request):
    return render(request, 'pages/phoneLogIn.html')

def logout(request):
    # if request.method == 'POST':
    auth.logout(request)

    return redirect('login')
