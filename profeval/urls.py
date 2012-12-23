from django.conf.urls import patterns, include, url
from django.conf import settings
from haystack.views import SearchView
from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet

from evals.views import SearchWithRequest

from evals.views import home, done, logout, error, form, form2
from evals.facebook import facebook_view

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'evals.views.home', name='home'),
    url(r'^professor/(\d+)/$', 'evals.views.professor', name='professor'),
    url(r'^add_comment/$', 'evals.views.add_comment', name='add_comment'),
    url(r'^update_profrating/$', 'evals.views.update_profrating', name='update_profrating'),
    url(r'^get_search_data/$', 'evals.views.get_search_data', name='get_search_data'),
    #(r'^search/', include('haystack.urls')),
    #url(r'^search/', include('evals.haystack_urls')),
    url(r'^search/', 'evals.views.SearchWithRequest',name='haystack_search'),
    url(r'', include('social_auth.urls')),
    url(r'^done/$', done, name='done'),
    url(r'^error/$', error, name='error'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^form/$', form, name='form'),
    url(r'^form2/$', form2, name='form2'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fb/', facebook_view, name='fb_app'),


    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin_tools/', include('admin_tools.urls')),

    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='auth_logout'),
    url(r'^logout/(?P<next_page>.*)/$', 'django.contrib.auth.views.logout', name='auth_logout_next'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)
