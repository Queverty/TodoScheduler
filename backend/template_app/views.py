import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
import requests
from django.contrib import messages
from users.models import User


# Create your views here.


class IndexView(View):

	def get(self, request):
		if request.user.is_anonymous:
			return render(request, "template_app/index.html")
		day = requests.get('http://localhost:8000/api/task-day/', params={'user': request.user.id}).json()
		week = requests.get('http://localhost:8000/api/task-week/', params={'user': request.user.id}).json()
		month = requests.get('http://localhost:8000/api/task-month/', params={'user': request.user.id}).json()
		return render(request, "template_app/index_log.html",
					  context={'day': day,
							   'week': week,
							   'month': month})

	def post(self, request):
		task = request.POST.get('Title')
		description = request.POST.get('Description')
		if request.POST.get('month'):
			url = 'http://localhost:8000/api/task-month/'
		elif request.POST.get('day'):
			url = 'http://localhost:8000/api/task-day/'
		elif request.POST.get('week'):
			url = 'http://localhost:8000/api/task-week/'
		data = {'title': task, 'description': description, 'user': request.user.id}
		response = requests.post(url, data=data)
		data = response.json()
		if response.status_code != 201:
			messages.add_message(request, messages.INFO, data)
		return HttpResponseRedirect(request.META['HTTP_REFERER'])



class AboutView(View):

	def get(self, request):
		return render(request, 'template_app/about.html')


class UserTopTableView(View):

	def get(self, request):
		response = requests.get('http://localhost:8000/api/users/')
		data = response.json()
		return render(request, 'template_app/top_users.html', context={'users': data})
