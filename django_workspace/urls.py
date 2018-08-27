"""django_workspace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

#from restraunts.views import home_function_view, about_function_view, contact_function_view
#from restraunts.views import home_class_view, about_class_view, contact_class_view
#from restraunts.views import home_template_view, about_template_view, contact_template_view
#from restraunts.views import home_list_view, about_list_view, contact_list_view

#from restraunts.views import all_list_view, about_template_view, contact_template_view, dinein_list_view, takeaway_list_view, dhabha_list_view
from restraunts.views import  generalised_list_view, about_template_view, contact_template_view , all_list_view

'''from restraunts.views import(HomeListView,
HomeDetailView,
ContactTemplateView,
AboutTemplateView
HomeTemplateView_dinein,
HomeTemplateView_dhabha,
HomeTemplateView_takeaway)'''
                            
                    

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    # URL for Function View
    #url(r'^home/', home_function_view),
    #url(r'^about/', about_function_view),
    #url(r'^contact/', contact_function_view),
    
    # URL for Class Based View
    #url(r'^', home_class_view.as_view()),
    #url(r'^about/', about_class_view.as_view()),
    #url(r'^contact/', contact_class_view.as_view()),
    
    # URL for Class Based Template View
    #url(r'^home/', home_template_view.as_view()),
    #url(r'^about/', about_template_view.as_view()),
    #url(r'^contact/', contact_template_view.as_view()),
    
    # URL for Class Based List View
    url(r'^home/$', all_list_view.as_view()),
    url(r'^about/$', about_template_view.as_view()),
    url(r'^contact/$', contact_template_view.as_view()),
    #url(r'^dinein/', dinein_list_view.as_view()),
    #url(r'^dhabha/', dhabha_list_view.as_view()),
    #url(r'^takeaway/', takeaway_list_view.as_view()),
    url(r'^home/(?P<slug>[\w-]+)', generalised_list_view.as_view()),
    
    
    ]
    
    



























'''url(r'^$', HomeListView.as_view()),
url(r'^(?P<slug>\w+)/$', HomeListView.as_view()),    
url(r'^detail/(?P<pk>\w+)/$', HomeDetailView.as_view()),    
url(r'^about/$', AboutTemplateView.as_view()),
url(r'^contact/$', ContactTemplateView.as_view()),
url(r'^home/dinein/$', HomeTemplateView_dinein.as_view()),
url(r'^home/dhabha/$', HomeTemplateView_dhabha.as_view()),
url(r'^home/takeaway/$', HomeTemplateView_takeaway.as_view()),'''
