from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^(?P<question_id>[0-9]+)/list$', views.answer_list, name='answer_list'),
	url(r'^(?P<answer_id>[0-9]+)/$', views.answer_details, name='answer_details'),
	url(r'^(?P<question_id>[0-9]+)/addt$', views.answer_list, name='add_answer'),
]