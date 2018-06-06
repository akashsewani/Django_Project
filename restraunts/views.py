from django.shortcuts import render

#from django.http import HttpResponse,HttpResponseNotFound

from django.views.generic import View



#def home_function(request):
#	return render(request,"home.html",{})
	#return HttpResponse("Hello! It worked");
	#return HttpResponseNotFound("<h1>NotFound</h1>")
	#return HttpResponse(status=503)


# Create your views here.


#def about_function(request):
#	return render(request,"about.html",{})
	


#def contact_function(request):
#	return render(request,"contact.html",{})


class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "home.html",{})

class ContactView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "contact.html",{})


class AboutView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "about.html",{})