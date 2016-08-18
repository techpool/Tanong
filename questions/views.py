from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Question
from .serializers import QuestionSerializer

class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
@login_required(login_url='/auth/login')
def question_list(request):
	"""
	List all code snippets, or create a new snippet.
	"""
	if request.method == 'GET':
		questions = Question.objects.all()
		print(questions[0].user)
		serializer = QuestionSerializer(questions, many=True)
		return JSONResponse(serializer.data)
	else:
		return HttpResponse(status=403)