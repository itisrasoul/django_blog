#Import modules
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'Rasoul',
        'age': '15',
    }
    return render(request, 'index.html', context)