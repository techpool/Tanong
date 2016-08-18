from django.db import models
from questions.models import Question
from django.contrib.auth.models import User
# Create your models here.

class Answer(models.Model):
	text = models.CharField(max_length=1000)
	upvote = models.IntegerField(required=True, default=0)
	downvote = models.IntegerField(required=True, default=0)
	comment_count = models.IntegerField(required=True, default=0)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(
			User,
			on_delete=models.CASCADE,
			verbose_name='the related User'
		)
	question = models.ForeignKey(
			Question,
			related_name='answer',
			on_delete=models.CASCADE,
			verbose_name='the related Question'
		)

class Comment(models.Model):
	text = models.CharField(max_length=1000)
	upvote = models.IntegerField(required=True, default=0)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(
			User,
			on_delete=models.CASCADE,
			verbose_name='the related User'
		)
	answer = models.ForeignKey(
			Answer,
			on_delete=models.CASCADE,
			related_name='comments',
			verbose_name='the related answer'
		)