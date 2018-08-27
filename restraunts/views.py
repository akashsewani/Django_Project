from django.shortcuts import render

from django.views.generic import View

from django.views.generic import TemplateView

from django.views.generic import ListView

from django.db.models import Q

from .models import RestrauntInfo


# Create your views here.
#Function Based View
'''def home_function_view(request):
	return render(request,"home.html",{})
	
def contact_function_view(request):
	return render(request,"contact.html",{})
	
def about_function_view(request):
	return render(request,"about.html",{})'''
	

#Class Based View
'''class home_class_view(View):
	def get(self, request, *args, **kwargs):
		return render(request,"home.html",{})

class about_class_view(View):
	def get(self, request, *args, **kwargs):
		return render(request,"about.html",{})

class contact_class_view(View):
	def get(self, request, *args, **kwargs):
		return render(request,"contact.html",{})'''


'''#Class Based Template View		
class home_template_view(TemplateView):
	template_name="home.html"
	def get_context_data(self,*args,**kwargs):
		queryset=RestrauntInfo.objects.all()
		context=super(home_template_view,self).get_context_data(*args,**kwargs)
		context={
				"object_list":queryset
			}
		return context

class about_template_view(TemplateView):
	template_name="about.html"

class contact_template_view(TemplateView):
	template_name="contact.html"'''
		
		
#Class Based List View		
class all_list_view(ListView):
	template_name="home.html"
	queryset=RestrauntInfo.objects.all()
	
'''class dinein_list_view(ListView):
	template_name="home.html"
	queryset=RestrauntInfo.objects.all().filter(Category__iexact='Dinein')  #double underscores

class takeaway_list_view(ListView):
	template_name="home.html"
	queryset=RestrauntInfo.objects.all().filter(Category__iexact='takeaway')  #double underscores

class dhabha_list_view(ListView):
	template_name="home.html"
	queryset=RestrauntInfo.objects.all().filter(Category__iexact='dhabha') #double underscores'''

class about_template_view(TemplateView):
	template_name="about.html"
	def get_context_data(self, *args, **kwargs):
		context=super(about_template_view,self).get_context_data(*args,**kwargs)
		context={
			"pagename":"about page"
		}
		return context

class contact_template_view(TemplateView):
	template_name="contact.html"
	def get_context_data(self, *args, **kwargs):
		context=super(contact_template_view,self).get_context_data(*args,**kwargs)
		context={
			"pagename":"contact page"
		}
		return context
		
class generalised_list_view(ListView):
	template_name="home.html"
	def get_queryset(self,**kwargs):
		slug=self.kwargs.get("slug")
		print("akash sew")
		print(self.kwargs)
		print(self.args)
		if(slug):
			queryset=RestrauntInfo.objects.all().filter(
				Q(Category__iexact=slug)#|
			#	Q(Category__icontains=slug)
				)
		else:
			queryset=RestrauntInfo.objects.all()
		return queryset
	
		
	
	

	
