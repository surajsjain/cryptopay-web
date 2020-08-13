from django.shortcuts import render, redirect

from usermgmt.models import APIAccessKey
from usermgmt.utils import generate_key

# Create your views here.
def displayPayments(request):
    ctxt = {
        'nav_active' : 'Transactions',
    }
    return render(request, 'dashboard/transactions.html', context=ctxt)

def displayAPIKeys(request):
    api_keys = []
    try:
        api_keys = APIAccessKey.objects.filter(user = request.user)
    except:
        pass

    ctxt = {
        'nav_active' : 'APIKeys',
        'api_keys' : api_keys,
    }

    return render(request, 'dashboard/api_keys.html', context=ctxt)

def newAPIKey(request):

    if request.method == 'GET':
        ctxt = {
            'nav_active' : 'APIKeys',
        }

        return render(request, 'dashboard/new_api_key.html', context=ctxt)

    else:
        name = request.POST['name']
        user = request.user
        userName = user.username
        api_key = generate_key(userName)

        access_key = APIAccessKey()
        access_key.user = user
        access_key.name = name
        access_key.key = api_key
        access_key.save()

        return redirect('api_keys')

def deleteAPIKey(request, key_id):
    apikey = APIAccessKey.objects.get(id = key_id)
    apikey.delete()

    return redirect('api_keys')
