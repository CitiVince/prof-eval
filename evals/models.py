from django.db import models
from decimal import *
import fields

#social auth custom user classes
class CustomUserManager(models.Manager):
    def create_user(self, username, email):
        return self.model._default_manager.create(username=username)


class CustomUser(models.Model):
    username = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)

    objects = CustomUserManager()

    def is_authenticated(self):
        return True

class Professor(models.Model):
    #METHODS

    def calculate_ratings(self, prof_id):
        #ini stuff
        rating_sum_clarity = 0
        rating_sum_interesting = 0
        rating_sum_easiness = 0
        rating_sum_nicess = 0
        rating_all = []

        #get all rating info for prof
        comment_info = Comment.objects.filter(professor_id=prof_id)
        nComments = len(comment_info)

        for comment in comment_info:
            rating_sum_clarity += comment.rating_clarity
            rating_sum_interesting += comment.rating_interesting
            rating_sum_easiness += comment.rating_easiness
            rating_sum_nicess += comment.rating_niceness

        getcontext().prec = 3
        #get overall_rating:
        rating_all.append(['Gesamt:',Decimal((rating_sum_clarity+rating_sum_interesting+rating_sum_easiness+rating_sum_nicess) / (nComments*4))])

        #get sub ratings
        rating_all.append(['Klarheit:' ,rating_sum_clarity / nComments])
        rating_all.append(['Interessant:', rating_sum_interesting / nComments])
        rating_all.append(['Einfacheit:', rating_sum_easiness / nComments])
        rating_all.append(['Nettigkeit:',rating_sum_nicess / nComments])
        return rating_all


    #FIELDS
    #Choices
    DEPARTMENT_CHOICES = (
            ('Rechtswissenschaften', 'Rechtswissenschaften'),
            ('Sozialwissenschaften', 'Sozialwissenschaften'),
            ("Wirtschaftswissenschaften", 'Wirtschaftswissenschaften'),
            )
    #Fields
    pre_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    university = models.ForeignKey('University', null=True, blank=True)
    department = models.CharField(choices = DEPARTMENT_CHOICES, max_length=200)
    photo = models.ImageField(upload_to='profs', null=True, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)

    def __unicode__(self):
        return self.last_name

class University(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='profs', null=True, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False, blank=True, null=True)
    def __unicode__(self):
        return self.name


class Comment(models.Model):


    professor = models.ForeignKey('Professor', null=True, blank=True)
    review = models.CharField(max_length=1000)
    course = models.CharField(max_length=200)
    rating_overall = models.IntegerField()
    rating_clarity = models.IntegerField()
    rating_interesting = models.IntegerField()
    rating_easiness = models.IntegerField()
    rating_niceness = models.IntegerField()
    user = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)