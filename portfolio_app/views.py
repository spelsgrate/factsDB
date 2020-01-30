from django.shortcuts import render, redirect
from portfolio_app.models import Facts

def index(request):
    return render(request, 'portfolio.html')

def facts(request):
    names = Facts.objects.all()
    name_list = Facts.objects.values_list('name', flat=True).all
    context = {
        'names': names
    }
    print(context)
    return render(request, 'facts.html', context)

def factsSubmit(request):
    print("*********")
    print(request.GET)
    print("*********")

    #query = request.GET.get('country')
    country = Facts.objects.get(id=request.GET['country'])
    context = {
        'country': country
    }
    print(country)
    return render(request, 'facts_submit.html', context)
