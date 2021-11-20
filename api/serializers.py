from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
            model = Movie
            fields = ('pk','task_number', 'task_name', 'task_description', 'deadline')