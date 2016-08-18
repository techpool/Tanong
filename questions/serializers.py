from rest_framework import serializers
from .models import Question, Comment
from django.contrib.auth.models import User	

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ('id', 'text', 'question', 'user')

class QuestionSerializer(serializers.ModelSerializer):
	comments = CommentSerializer(
		many=True,
		read_only=True
	)

	class Meta:
		model = Question
		fields = ('id', 'question_text', 'question_description', 'created', 'updated', 'user', 'upvote', 'downvote', 'comments')
		depth = 1