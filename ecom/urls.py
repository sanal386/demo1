"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from publicapp.views import *
from userapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'base/$',base,),
    url(r'available/$',available,name="available"),
    url(r'login/$',login,name="login"),
    url(r'registration',registration,name="registration"),
    url(r'fruits/$',fruits,name="fruits"),
    url(r'apple/$',apple,name="apple"),
    url(r'orange/$',orange, name="orange"),
    url(r'grape/$',grape, name="grape"),
    url(r'vegetables/$',vegetables,name="vegetables"),
    url(r'tomato/$',tomato,name="tomato"),
    url(r'potato/$',potato,name="potato"),
    url(r'bittergourd/$',bitter,name="bitter"),
    url(r'electronics/$',electronics,name="electro"),
    url(r'mobile/$',mobile,name="mobile"),
    url(r'television/$',tv,name="tv"),
    url(r'fridge/$',fridge,name="fridge"),
    url(r'wash',wash,name="wash"),
    url(r'groceries/$',groceries,name="groceries"),
    url(r'atta/$',atta,name="atta"),
    url(r'maida/$',maida,name="maida"),
    url(r'rice/$',rice,name="rice"),
]
