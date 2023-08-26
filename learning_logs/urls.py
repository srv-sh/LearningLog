"""Define URL patterns for learning_logs. """

# from django.conf.urls import url 
from django.urls import re_path as url
from . import views

urlpatterns = [
    # Home page
    url(r'^$', views.index, name = 'index')
]