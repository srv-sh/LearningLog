"""Define URL patterns for learning_logs. """

# from django.conf.urls import url 
from django.urls import re_path as url
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # Home page
    url(r'^$', views.index, name = 'index'),
    url(r'^topics/$', views.topics, name = 'topics'),
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    #Page for adding a new topic 
    url(r'^new_topic/$', views.new_topic , name = 'new_topic'),
    #page for adding a new entry to a topic
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry , name = 'new_entry'),
    # page for editing an entry
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name = 'edit_entry'),
]