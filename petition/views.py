from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def vote(request):
    return render(request, 'vote.html')