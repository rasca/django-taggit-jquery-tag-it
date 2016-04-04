from django.conf.urls import *
from taggit_autocomplete.views import list_tags

urlpatterns = [
    url(r'^list/$', list_tags, name='taggit_autocomplete-list'),
]
