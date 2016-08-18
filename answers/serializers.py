from rest_framework import serializers
from .models import Answer, Comment

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ('id', 'text', 'answer', 'user')

class AnswerSerializer(serializers.ModelSerializer):
	comments = CommentSerializer(
		many=True,
		read_only=True
	)

	class Meta:
		model = Answer
		fields = ('id', 'text', 'upvote', 'downvote', 'created', 'updated', 'user', 'question', 'comments')
		depth =1