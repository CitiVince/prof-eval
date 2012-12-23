from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext
from django.template import Context, loader
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django import forms
from django.core import serializers
import json
import collections

from evals.models import Professor, University, Comment
from haystack.views import SearchView
from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet

#social auth imports
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages.api import get_messages

from social_auth import __version__ as version
from social_auth.utils import setting

def SearchWithRequest(request):

    __name__ = 'SearchWithRequest'

    sqs = SearchQuerySet().autocomplete(name_auto=request.GET.get('q', ''))
    return render_to_response('content/home.html', {"sqs":sqs}, context_instance=RequestContext(request))


#extend search view with autocomplete
"""
class SearchWithRequest(SearchView):
    
    __name__ = 'SearchWithRequest'

    def build_form(self, form_kwargs=None):
        if form_kwargs is None:
            form_kwargs = {}
            
        if self.searchqueryset is None:
            sqs = SearchQuerySet().autocomplete(name_auto=self.request.GET.get('q', ''))
            form_kwargs['searchqueryset'] = sqs
        
        return super(SearchWithRequest, self).build_form(form_kwargs)
"""

def home(request):
    """Home view, displays login mechanism"""
    if request.user.is_authenticated():
        return HttpResponseRedirect('done')
    else:
        return render_to_response('content/home.html', {'version': version},
                                  RequestContext(request))


@login_required
def done(request):
    """Login complete view, displays user data"""
    ctx = {
        'version': version,
        'last_login': request.session.get('social_auth_last_login_backend')
    }
    return render_to_response('content/done.html', ctx, RequestContext(request))


def error(request):
    """Error view"""
    messages = get_messages(request)
    return render_to_response('content/error.html', {'version': version,
                                             'messages': messages},
                              RequestContext(request))


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')


def form(request):
    if request.method == 'POST' and request.POST.get('username'):
        name = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
        request.session['saved_username'] = request.POST['username']
        backend = request.session[name]['backend']
        return redirect('socialauth_complete', backend=backend)
    return render_to_response('content/form.html', {}, RequestContext(request))


def form2(request):
    if request.method == 'POST' and request.POST.get('first_name'):
        request.session['saved_first_name'] = request.POST['first_name']
        name = setting('SOCIAL_AUTH_PARTIAL_PIPELINE_KEY', 'partial_pipeline')
        backend = request.session[name]['backend']
        return redirect('socialauth_complete', backend=backend)
    return render_to_response('content/form2.html', {}, RequestContext(request))


def professor(request, prof_id=None):
    if not prof_id:
        prof_id = 0
    else:
        prof_id = int(prof_id)

    prof_info = Professor.objects.get(id=prof_id)
    comment_info = Comment.objects.filter(professor_id=prof_id)

    #get prof ratings
    prof = Professor()
    prof_rating = prof.calculate_ratings(prof_id)
    
    return render_to_response('content/professor.html', {
            "prof_info":prof_info,
            "prof_rating":prof_rating,
            "comment_info":comment_info,
            "prof_id":prof_id}, context_instance=RequestContext(request))

def update_profrating(request):
    prof_id = int(request.POST['prof_id'])
    #get prof ratings
    prof = Professor()
    prof_rating = prof.calculate_ratings(prof_id)

    return render_to_response('content/done_profrating.html', {"prof_rating":prof_rating}, RequestContext(request))

def add_comment(request):

    #get post data
    amount_easiness = int(request.POST['amount_easiness'])
    amount_clarity = int(request.POST['amount_clarity'])
    amount_interesting = int(request.POST['amount_interesting'])
    amount_niceness = int(request.POST['amount_niceness'])
    prof_id = int(request.POST['prof_id'])
    course = request.POST['course']
    comment = request.POST['comment']
    comment_info = Comment.objects.filter(professor_id=prof_id)
   
    #get profs name with id
    prof_name = Professor.objects.get(id=prof_id)

    #calculate average
    rating_overall = (amount_easiness + amount_clarity + amount_interesting + amount_niceness)  / 4

    #insert data
    q = Comment(review=comment, rating_overall=rating_overall, rating_clarity=amount_clarity, rating_interesting=amount_interesting, rating_easiness=amount_easiness, rating_niceness=amount_niceness, course=course, professor=prof_name)
    q.save()

    return render_to_response('content/done_rating.html', {"comment_info":comment_info}, RequestContext(request))

def get_search_data(request):
    #ini
    search_list = []
    #define fields
    prof_fields = ['pre_name', 'last_name']
    all_profs = json.loads(serializers.serialize("json", Professor.objects.all(),fields=('last_name','pre_name')))


    for prof in all_profs:
        print prof
        current_prof = str(prof['fields']['pre_name']) + " " + str(prof['fields']['last_name'])
        search_list.append(current_prof)

    #convert data
    def convert(data):
        if isinstance(data, unicode):
            return str(data)
        elif isinstance(data, collections.Mapping):
            return dict(map(convert, data.iteritems()))
        elif isinstance(data, collections.Iterable):
            return type(data)(map(convert, data))
        else:
            return data
    #search_list = json.dumps(search_list)
    print search_list

    return render_to_response('content/get_search_data.html', {"search_list":search_list}, RequestContext(request))








