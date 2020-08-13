from django.shortcuts import render, redirect

# Create your views here.
def displayPayments(request):
    ctxt = {
        'nav_active' : 'Transactions',
    }
    return render(request, 'dashboard/dash_home.html', context=ctxt)
