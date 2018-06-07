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

#from restraunts.views import home_function, about_function, contact_function
#from restraunts.views import HomeView,ContactView, AboutView
from restraunts.views import HomeTemplateView,ContactTemplateView,AboutTemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/$', HomeTemplateView.as_view()),
    url(r'^about/$', AboutTemplateView.as_view()),
    url(r'^contact/$', ContactTemplateView.as_view()),
]
