from django.shortcuts import render

from django.http import HttpResponse,HttpResponseNotFound

from django.views.generic import View

from django.views.generic import TemplateView

from django.views.generic import ListView

from .models import RestrauntInfo
# Create your views here.



# Function based views
'''def home_function(request):
	return render(request,"home.html",{})
	#return HttpResponse("Hello! It worked");
	#return HttpResponseNotFound("<h1>NotFound</h1>")
	#return HttpResponse(status=503)

def about_function(request):
	return render(request,"about.html",{})
	
def contact_function(request):
	return render(request,"contact.html",{})
'''


#Class based views
'''
class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "home.html",{})

class ContactView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "contact.html",{})


class AboutView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "about.html",{})
'''


#TemplateView based views
'''class HomeTemplateView(TemplateView):
	template_name="home.html"
	
	def get_context_data(self,*args,**kwargs):
		context=super(HomeTemplateView,self).get_context_data(*args,**kwargs)
		queryset=RestrauntInfo.objects.all()
		context={
					"pagename":"Home Page",
					"objectlist" : queryset
				}
		return context
		
		
class HomeTemplateView_dhabha(TemplateView):
	template_name="home.html"
	
	def get_context_data(self,*args,**kwargs):
		context=super(HomeTemplateView_dhabha,self).get_context_data(*args,**kwargs)
		queryset=RestrauntInfo.objects.all().filter(Category__iexact="dhabha")
		context={
					"pagename":"Home Page",
					"objectlist" : queryset
				}
		return context
		
		
class HomeTemplateView_dinein(TemplateView):
	template_name="home.html"
	
	def get_context_data(self,*args,**kwargs):
		context=super(HomeTemplateView_dinein,self).get_context_data(*args,**kwargs)
		queryset=RestrauntInfo.objects.all().filter(Category__iexact="dinein")
		context={
					"pagename":"Home Page",
					"objectlist" : queryset
				}
		return context
		
		
class HomeTemplateView_takeaway(TemplateView):
	template_name="home.html"
	
	def get_context_data(self,*args,**kwargs):
		context=super(HomeTemplateView_takeaway,self).get_context_data(*args,**kwargs)
		queryset=RestrauntInfo.objects.all().filter(Category__iexact="take away")
		context={
					"pagename":"Home Page",
					"objectlist" : queryset
				}
		return context'''
		
		
		
class HomeListView(ListView):
	template_name="home.html"
	context_object_name='objectlist'
	
	def get_queryset(self):

		slug=self.kwargs.get("slug")
		print slug

		if slug:
			queryset=RestrauntInfo.objects.all().filter(Category__iexact=slug)
		else :
			queryset=RestrauntInfo.objects.all()
		return queryset


			
		
		

			
		
		
		
	
class AboutTemplateView(TemplateView):
	template_name="about.html"
	
	def get_context_data(self,*args,**kwargs):
		context=super(AboutTemplateView,self).get_context_data(*args,**kwargs)
		print args
		print kwargs
		context={
					"pagename":"About Page"
				}
		return context
		
		

class ContactTemplateView(TemplateView):
	template_name="contact.html"
	
	def get_context_data(self,*args,**kwargs):
		context=super(ContactTemplateView,self).get_context_data(*args,**kwargs)
		context={
					"pagename":"Contact Page"
				}
		return context

