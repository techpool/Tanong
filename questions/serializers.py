from rest_framework import serializers
from .models import Question

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)

class QuestionSerializer(serializers.Serializer):
	pk = serializers.IntegerField(read_only=True)
	question_text = serializers.CharField(required=True, max_length=200)
	question_description = serializers.CharField(required=False, allow_blank=True, max_length=400)
	user = UserSerializer()
	created = serializers.DateTimeField(read_only=True)

	def create(self, validated_data):
		"""
		Create and return a new `Snippet` instance, given the validated data.
		"""
		return Question.objects.create(**validated_data)

	def update(self, instance, validated_data):
		"""
		Update and return an existing `Snippet` instance, given the validated data.
		"""
		instance.question_text = validated_data.get('question_text', instance.question_text)
		instance.question_description = validated_data.get('question_description', instance.question_description)
		instance.save()
		return instance