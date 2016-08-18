from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^list/', views.question_list, name='index')
]