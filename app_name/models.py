from django.db import models

# Create your models here.aaaaa
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    bbb = models.IntegerField()
    aaa = models.IntegerField()