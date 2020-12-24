from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Group(models.Model):
    group_name = models.CharField(max_length=32)

    def __str__(self):
        return self.group_name


class Note(models.Model):
    title = models.CharField(max_length=128)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']