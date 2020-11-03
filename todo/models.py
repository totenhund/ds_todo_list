from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text
