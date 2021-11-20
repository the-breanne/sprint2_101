
# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.
class Movie(models.Model):
    task_number = models.CharField(max_length=50)
    task_name = models.TextField(max_length=360)
    task_description = models.TextField(max_length=360)
    deadline = models.TextField(max_length=360)

    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()
