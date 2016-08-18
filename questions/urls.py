from django.conf.urls import url

from . import views

urlpatterns = [
	# questions api
	url(r'^list/$', views.question_list, name='question_list'),
	url(r'^(?P<question_id>[0-9]+)/$', views.question_details, name='question_details'),
	url(r'^add', views.add_question, name='add_question'),

	# comment api
	url(r'^(?P<question_id>[0-9]+)/comments$', views.comments, name='list_comments'),

	# upvote & downvote
	# url(r'^(?P<question_id>[0-9]+)/upvote$', views.upvote, name='list_comments'),	
	# url(r'^(?P<question_id>[0-9]+)/downvote$', views.downvote, name='list_comments'),
]