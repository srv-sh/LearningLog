"""Define URL patterns for learning_logs. """

# from django.conf.urls import url 
from django.urls import re_path as url
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    url(r'^$', views.index, name = 'index'),
    url(r'^topics/$', views.topics, name = 'topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic')
]