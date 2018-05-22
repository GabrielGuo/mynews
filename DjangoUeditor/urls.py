#coding:utf-8
import os
from django import VERSION
if VERSION[0:2]>(1,3):
    from django.conf.urls import  url
else:
    from django.conf.urls.defaults import  url

from views import get_ueditor_controller
from django.conf import settings

urlpatterns = [
    url(r'^controller/$',get_ueditor_controller)
]
