from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import UsersSerializer, TaskPerDaySerializer, TaskPerWeekSerializer, TaskPerMonthSerializer, \
	TaskPerMonthCreateSerializer, TaskPerDayCreateSerializer, TaskPerWeekCreateSerializer, ProductSerializers, \
	InventorySerializers
from users.models import User, Inventory
from .services.taskday import TaskPerDayService
from .services.taskmonth import TaskPerMonthService
from .services.taskweek import TaskPerWeekService
from .services.task_day_complited import TaskPerDayComplitedService
from .services.task_week_complited import TaskPerWeekComplitedService
from .services.task_month_complited import TaskPerMonthComplitedService
from .services.task_deleted import TaskDeletedService
from .services.queryset_market import ProductQuerySetGetService
from .services.market_buy import ProductBayGetService
from .services.inventory_user import InventoryGetService
from .services.inventory_user_delete import InventoryDeleteService
from .services.user_subscribe import SubscribeService
from .services.user_unsubscribe import UnSubscribeService
from rest_framework.response import Response
from market.models import Product
from todolist_app.models import TaskPerMonth, TaskPerWeek, TaskPerDay
from users.models import Subscribe

class UsersAPIView(APIView):

	def get(self, request, *args, **kwargs):
		if request.GET.get('user'):
			user_id = request.GET.get('user')
		else:
			user_id = request.user.id
		user = User.objects.all()
		serializer = UsersSerializer(user, many=True, context={'user_id': user_id})
		return Response(serializer.data)


class UserProfileAPIView(APIView):

	def get(self, request, **kwargs):
		if request.GET.get('user_id'):
			user_id = request.GET.get('user_id')
		else:
			user_id = request.user.id
		user = User.objects.filter(id=user_id)
		serializer = UsersSerializer(user, many=True, context={'user_id': user_id})
		return Response(serializer.data)


class TaskPerDayAPIView(APIView):

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

	def put(self, request, *args, **kwargs):
		task_id = request.GET.get('task_id')
		user_id = request.GET.get('user_id')
		outcome = TaskPerDayComplitedService.execute(
			{'user_id': user_id, 'task_id': task_id})
		return Response(status=200)

	def delete(self, request, *args, **kwargs):
		task_id = request.GET.get('task_id')
		outcome = TaskDeletedService.execute({'task_id': task_id})
		return Response(status=200)


class TaskPerWeekAPIView(APIView):

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

	def put(self, request, *args, **kwargs):
		task_id = request.GET.get('task_id')
		user_id = request.GET.get('user_id')
		outcome = TaskPerWeekComplitedService.execute(
			{'user_id': user_id, 'task_id': task_id})
		return Response(status=200)

	def delete(self, request, *args, **kwargs):
		task_id = request.GET.get('task_id')
		outcome = TaskDeletedService.execute({'task_id': task_id})
		return Response(status=200)


class TaskPerMonthAPIView(APIView):

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

	def put(self, request, *args, **kwargs):
		task_id = request.GET.get('task_id')
		user_id = request.GET.get('user_id')
		outcome = TaskPerMonthComplitedService.execute(
			{'user_id': user_id, 'task_id': task_id})
		return Response(status=200)

	def delete(self, request, *args, **kwargs):
		task_id = request.GET.get('task_id')
		outcome = TaskDeletedService.execute({'task_id': task_id})
		return Response(status=200)


class MarketAPIView(APIView):

	def get(self, request):
		queryset = ProductQuerySetGetService.execute({})
		serializer = ProductSerializers(queryset, many=True)
		return Response(serializer.data)

	def put(self, request, *args, **kwargs):
		prod_id = request.GET.get('prod_id')
		user_id = request.GET.get('user_id')
		outcome = ProductBayGetService.execute({'user_id': user_id, 'product_id': prod_id})
		return Response(data=(outcome))


class InventoryAPIView(APIView):

	def get(self, request):
		user_id = request.GET.get('user_id')
		queryset = InventoryGetService.execute({'user_id':user_id})
		serializer = InventorySerializers(queryset, many=True)
		return Response(serializer.data)

	def delete(self, request, *args, **kwargs):
		user_id = request.GET.get('user_id')
		queryset = InventoryDeleteService.execute({'user_id':user_id})
		return Response(status=200)


class UserSubscribeAPIView(APIView):

	def get(self, request):
		author_id = request.GET.get('author')
		user_id = request.GET.get('user')
		queryset = SubscribeService.execute({'author_id':author_id,'user_id':user_id})
		return Response(status=201)

class UserUnSubscribeAPIView(APIView):

	def get(self, request):
		author_id = request.GET.get('author')
		user_id = request.GET.get('user')
		queryset = UnSubscribeService.execute({'author_id':author_id,'user_id':user_id})
		return Response(status=204)