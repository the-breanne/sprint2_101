
# Register your models here.
from django.contrib import admin
from .models import Movie

class MovieList(admin.ModelAdmin):
    list_display = ('task_number', 'task_name', 'task_description', 'deadline')
    list_filter = ('task_number', 'task_name', 'task_description', 'deadline')
    search_fields = ('task_number', 'task_name')
    ordering = ['task_number']


admin.site.register(Movie, MovieList)