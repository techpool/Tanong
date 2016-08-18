from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	question_description = models.CharField(max_length=400)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	upvote = models.IntegerField(default=0)
	downvote = models.IntegerField(default=0)
	comment_count = models.IntegerField(default=0)
	user = models.ForeignKey(
			User,
			on_delete=models.CASCADE,
			verbose_name='the related User'
		)

class Comment(models.Model):
	text = models.CharField(max_length=1000)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		verbose_name='the related User'
	)
	question = models.ForeignKey(
			Question,
			on_delete=models.CASCADE,
			related_name='comments',
			verbose_name='the related question'
		)

		