from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def home(request):
  return render(request, 'myfirst.html')
def members(request):
  return render(request, 'members.html')
def about(request):
  return render(request, 'about.html')