from django.shortcuts import render

from django.http import HttpResponse,HttpResponseNotFound

import random


def home_function(request):
	return render(request,"home.html",{})
	#return HttpResponse("Hello! It worked");
	#return HttpResponseNotFound("<h1>NotFound</h1>")
	#return HttpResponse(status=503)


# Create your views here.


def about_function(request):
	return render(request,"about.html",{})
	


def contact_function(request):
	return render(request,"contact.html",{})
