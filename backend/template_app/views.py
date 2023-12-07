import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
import requests
from django.contrib import messages

from template_app.mixin import get_true_url_task
from users.models import User


# Create your views here.


class IndexView(View):

	def get(self, request):
		# if request.user.is_anonymous:
		# 	return render(request, "template_app/index.html")

		day = requests.get('http://localhost:8000/api/task-day/', params={'user': request.user.id},
						   headers={'Authorization': 'Token ce8686c517d20cde600cd9bb056181356df3e6c3'}).json()
		week = requests.get('http://localhost:8000/api/task-week/', params={'user': request.user.id},
							headers={'Authorization': 'Token ce8686c517d20cde600cd9bb056181356df3e6c3'}).json()
		month = requests.get('http://localhost:8000/api/task-month/', params={'user': request.user.id},
							 headers={'Authorization': 'Token ce8686c517d20cde600cd9bb056181356df3e6c3'}).json()
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
		response = requests.post(url, data=data,
							headers={'Authorization': 'Token ce8686c517d20cde600cd9bb056181356df3e6c3'})
		data = response.json()
		if response.status_code != 201:
			messages.add_message(request, messages.INFO, data)
		return HttpResponseRedirect(request.META['HTTP_REFERER'])


class AboutView(View):

	def get(self, request):
		return render(request, 'template_app/about.html')


class UserTopTableView(View):

	def get(self, request):
		response = requests.get('http://localhost:8000/api/users/', params={'user': request.user.id},
								headers={'Authorization': 'Token ce8686c517d20cde600cd9bb056181356df3e6c3'})
		data = response.json()
		return render(request, 'template_app/top_users.html', context={'users': data})


class UserProfilView(View):

	def get(self, request, **kwargs):
		response = requests.get(f'http://localhost:8000/api/user/{kwargs["pk"]}/', params={'user_id': kwargs["pk"]})
		data = response.json()
		return render(request, 'template_app/user_profile.html', context={'users': data})


class ProductListView(View):

	def get(self, request):
		response = requests.get('http://localhost:8000/api/products/').json()
		return render(request, 'template_app/market.html', context={'products': response})


class ProductBayView(View):

	def get(self, request, pk):
		response = requests.put('http://localhost:8000/api/products/',
								params={'prod_id': pk, 'user_id': request.user.id}).json()
		messages.add_message(request, messages.INFO, response)
		return HttpResponseRedirect(request.META['HTTP_REFERER'])


class TaskСompletedView(View):

	def get(self, request, **kwargs):
		url = get_true_url_task(kwargs)
		response = requests.put(url=url, params={'task_id': kwargs["pk"], 'user_id': request.user.id})
		return HttpResponseRedirect(request.META['HTTP_REFERER'])


class TaskDeletedView(View):

	def get(self, request, **kwargs):
		url = get_true_url_task(kwargs)
		response = requests.delete(url=url, params={'task_id': kwargs["pk"]})
		return HttpResponseRedirect(request.META['HTTP_REFERER'])


class InventoryView(View):

	def get(self, request):
		response = requests.get('http://localhost:8000/api/inventory/', params={'user_id': request.user.id}).json()
		return render(request, 'template_app/inventory.html', context={'inventory': response})


class InventoryDeleteView(View):

	def get(self, request):
		response = requests.delete('http://localhost:8000/api/inventory/',
								   params={'user_id': request.user.id})
		return HttpResponseRedirect(request.META['HTTP_REFERER'])


class UserRegisterView(View):

	def get(self, request):
		return render(request, 'template_app/register.html')

	def post(self, request):
		username = request.POST.get('txt')
		password = request.POST.get('pswd')
		email = request.POST.get('email')
		response = requests.post('http://localhost:8000/api/auth/users/',
								 data={'username': username, 'password': password, 'email': email})
		if response.status_code == 400:
			mes = response.json()
		else:
			mes = "Вы успешно Зарегистрировались! Теперь Вы можете зайти на свой аккаунт."
		messages.add_message(request, messages.INFO, mes)
		return HttpResponseRedirect(request.META['HTTP_REFERER'])


class UserLoginView(View):

	def get(self, request):
		return render(request, 'template_app/login.html')

	def post(self, request):
		username = request.POST.get('username')
		password = request.POST.get('pswd')
		response = requests.post('http://localhost:8000/api/auth/token/login/',
								 data={'username': username, 'password': password}).json()
		print(response)
		return render(request, 'template_app/login.html')
