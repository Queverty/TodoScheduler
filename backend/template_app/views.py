from django.shortcuts import render
from django.views import View
import requests

from users.models import User


# Create your views here.


class IndexView(View):


	def get(self, request):
		if request.user.is_anonymous:
			return render(request, "template_app/index.html")
		return render(request, "template_app/index_log.html")


class AboutView(View):

	def get(self, request):
		return render(request, 'template_app/about.html')


class UserTopTableView(View):

	def get(self, request):
		response = requests.get('http://localhost:8000/api/users/')
		data = response.json()
		return render(request, 'template_app/top_users.html', context={'users': data})
