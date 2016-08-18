from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Answer
from .serializers import AnswerSerializer

class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@login_required(login_url='/auth/login')
def answer_list(request, question_id):
	"""
	List all code snippets, or create a new snippet.
	"""
	if request.method == 'GET':
		answers = Answer.objects.filter(question=question_id)
		serializer = AnswerSerializer(answers, many=True)
		return JSONResponse(serializer.data)
	else:
		return HttpResponse(status=403)


@login_required(login_url='/auth/login')
def answer_details(request, answer_id):
	"""
	Retrieve, update or delete a code snippet.
	"""
	try:
		answer = Answer.objects.get(pk=answer_id)
	except Answer.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = AnswerSerializer(answer)
		return JSONResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = AnswerSerializer(answer, data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
		return JSONResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		answer.delete()
		return HttpResponse(status=204)