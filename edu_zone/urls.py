"""
URL configuration for edu_zone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import *
from django.conf.urls.static import *
from django.conf.urls import *
from django.conf import settings

from django.contrib.auth.urls import *
from edu_app.views import *
from edu_app.admin import *

urlpatterns = [
    path('edumanage/', admin.site.urls),
    
    path('', include('django.contrib.auth.urls')),
    
    path('',include('edu_app.h')),
    
    #path('', include('edu_app.h')),
   # path('payments/', include('django_razorpay.urls', namespace="django_razorpay")),
   
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

'''LOGIN_REDIRICT_URL=(('').replace('^','')).replace('(?P<path>.*)$','')
#LOGIN_URL='/login'
LOGOUT_REDIRICT_URL=(('').replace('^','')).replace('(?P<path>.*)$','')'''
#LOGOUT_URL='/logout'


#urlpatterns+=static((settings.LOGIN_REDIRICT_URL).replace('^','').replace('(?P<path>.*)$',''))
#urlpatterns+=static((settings.LOGIN_REDIRICT_URL).replace('^','').replace('(?P<path>.*)$',''))


handler400="edu_app.views.e400"
handler403="edu_app.views.e403"
handler404="edu_app.views.e404"
handler500="edu_app.views.e500"

'''
LOGIN_REDIRICT_URL='reg'
LOGIN_URL='/login'
LOGOUT_REDIRICT_URL='reg'''
