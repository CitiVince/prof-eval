from django.contrib import admin
from evals.models import Professor, University, Comment




class ProfessorAdmin(admin.ModelAdmin):
    fields = ['pre_name', 'last_name', 'university', 'department','photo']
    list_display = ['pre_name', 'last_name', 'university', 'department', 'created', 'updated','photo']
    search_fields = ['pre_name', 'last_name', 'university', 'department', 'created', 'updated']


class UniversityAdmin(admin.ModelAdmin):
    fields = ['name', 'location']
    list_display = ['name', 'location', 'created', 'updated']
    search_fields = ['name', 'location', 'created', 'updated']

class CommentAdmin(admin.ModelAdmin):
    fields = ['review', 'course', 'rating_overall', 'rating_clarity','rating_interesting','rating_easiness','rating_niceness', 'professor']
    list_display = ['review', 'course', 'rating_overall', 'rating_clarity','rating_interesting','rating_easiness','rating_niceness', 'created', 'updated', 'professor']
    search_fields = ['review', 'course', 'rating_overall', 'rating_clarity','rating_interesting','rating_easiness','rating_niceness', 'created', 'updated', 'professor']

    def prof_name(self, instance):
        return instance.professor.pre_name



admin.site.register(Professor, ProfessorAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(Comment, CommentAdmin)