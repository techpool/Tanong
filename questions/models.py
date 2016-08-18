from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_description = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
    		User,
    		on_delete=models.CASCADE,
    		verbose_name='the related User'
    	)