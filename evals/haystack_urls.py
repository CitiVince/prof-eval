from django.conf.urls import patterns, include, url

from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView

sqs = SearchQuerySet()

urlpatterns = patterns('haystack.views',
    url(r'^&', SearchView(load_all=False,searchqueryset=sqs),name='haystack_search'), 
)