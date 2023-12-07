from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import UsersSerializer, TaskPerDaySerializer, TaskPerWeekSerializer, TaskPerMonthSerializer, \
	TaskPerMonthCreateSerializer, TaskPerDayCreateSerializer, TaskPerWeekCreateSerializer
from users.models import User
from .services.taskday import TaskPerDayService
from .services.taskmonth import TaskPerMonthService
from .services.taskweek import TaskPerWeekService
from rest_framework.response import Response


class UsersViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UsersSerializer


class TaskPerDayView(APIView):

	def get(self, request, *args, **kwargs):
		if request.GET.get('user'):
			user_id = request.GET.get('user')
		else:
			user_id = request.user.id
		outcome = TaskPerDayService.execute({'user': user_id})
		serializer = TaskPerDaySerializer(outcome, many=True)
		return Response(serializer.data)

	def post(self, request, *args, **kwargs):
		serializer = TaskPerDayCreateSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data, status=201)
		return Response(serializer.errors, status=400)


class TaskPerWeekView(APIView):

	def get(self, request, *args, **kwargs):
		if request.GET.get('user'):
			user_id = request.GET.get('user')
		else:
			user_id = request.user.id
		outcome = TaskPerWeekService.execute({'user': user_id})
		serializer = TaskPerWeekSerializer(outcome, many=True)
		return Response(serializer.data)

	def post(self, request, *args, **kwargs):
		serializer = TaskPerWeekCreateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=201)
		return Response(serializer.errors, status=400)


class TaskPerMonthView(APIView):

	def get(self, request, *args, **kwargs):
		if request.GET.get('user'):
			user_id = request.GET.get('user')
		else:
			user_id = request.user.id
		outcome = TaskPerMonthService.execute({'user': user_id})
		serializer = TaskPerMonthSerializer(outcome, many=True)
		return Response(serializer.data)

	def post(self, request, *args, **kwargs):
		serializer = TaskPerMonthCreateSerializer(data=request.data,
												  context={'user': request.data['user']})
		if serializer.is_valid(raise_exception=True):
			serializer.save()
			return Response(serializer.data, status=201)
		return Response(serializer.errors, status=400)
