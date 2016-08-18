from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Question, Comment
from django.contrib.auth.models import User
from .serializers import QuestionSerializer, CommentSerializer

class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@login_required(login_url='/auth/login')
def question_list(request):
	if request.method == 'GET':
		questions = Question.objects.all()
		serializer = QuestionSerializer(questions, many=True)
		return JSONResponse(serializer.data)
	else:
		return HttpResponse(status=403)


@login_required(login_url='/auth/login')
def question_details(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = QuestionSerializer(question)
		return JSONResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = QuestionSerializer(question, data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
		return JSONResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		question.delete()
		return HttpResponse(status=204)

@login_required(login_url='/auth/login')
@csrf_exempt
def add_question(request):
	if request.method == 'POST':
		json_data = JSONParser().parse(request)
		data = {
			'question_text': json_data['question_text'],
			'question_description': json_data['question_description'],
			'user': request.user.pk
		}
		serializer = QuestionSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
		return JSONResponse(serializer.errors, status=400)

@login_required(login_url='/auth/login')
@csrf_exempt
def comments(request, question_id):
	if request.method == 'POST':
		json_data = JSONParser().parse(request)
		data = {
			'text': json_data['text'],
			'question': question_id,
			'user': request.user.pk
		}
		serializer = CommentSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
		return JSONResponse(serializer.errors, status=400)
	elif request.method == 'GET':
		try:
			comments = Comment.objects.filter(question=question_id)
		except Comment.DoesNotExist:
			return HttpResponse(status=404)
		serializer = CommentSerializer(comments, many=True)
		return JSONResponse(serializer.data)


# @login_required(login_url='/auth/login')
# @csrf_exempt
# def upvote(request, question_id):
# 	if request.method == 'GET':
# 		