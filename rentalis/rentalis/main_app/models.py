from django.contrib.auth.models import User
from django.db import models

class Profile(User):
    identity_document= models.IntegerField(max_length=10)
    birth_day = models.DateField()
    
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
