from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
import os

# Create your views here.

def intex(request):
    return render(request,'index.html')