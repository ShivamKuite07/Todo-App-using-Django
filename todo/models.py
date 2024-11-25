from django.db import models
from datetime import datetime

# Create your models here.

class Todos(models.Model):
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(default= datetime.now, blank=True)

    def __str__(self):
        return self.message  # This will make it easier to identify entries in the admin interface

