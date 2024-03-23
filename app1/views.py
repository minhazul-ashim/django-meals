from django.shortcuts import render
from django.http import HttpResponse
import datetime;

# Create your views here.
def index(request) :
    context = {
        "food" : "this is food",
        "value": 2,
        "items": [2,4,5,6,6],
    }
    return render(request, 'index.html', context)