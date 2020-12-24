from django.db import models


# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=100)
    id_num = models.CharField(max_length=100)
    fee = models.CharField(max_length=100)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.name
