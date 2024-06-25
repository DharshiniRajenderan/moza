from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def home(request):
	return render(request,"moza/home.html")
