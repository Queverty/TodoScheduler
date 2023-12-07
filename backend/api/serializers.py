import json

from djoser.serializers import UserSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from market.models import Product
from todolist_app.models import TaskPerDay, BaseTask, TaskPerWeek, TaskPerMonth
from users.models import User, Subscribe, Inventory


class UsersSerializer(serializers.ModelSerializer):
	is_subscribed = serializers.SerializerMethodField()
	followers = serializers.SerializerMethodField()

	class Meta:
		model = User
		fields = (
			'id', 'username', 'first_name', 'last_name', 'email', 'balance', 'points', 'rank', 'is_subscribed',
			'followers')

	def get_is_subscribed(self, obj):

		user_id = self.context.get('user_id')
		user = User.objects.get(id=user_id)
		if user.is_anonymous:
			return False
		return Subscribe.objects.filter(user=user, author=obj).exists()

	def get_followers(self, obj):
		return Subscribe.objects.filter(user=obj).count()


class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = BaseTask
		fields = ('title', 'description', 'is_completed', 'id')


class TaskPerDaySerializer(TaskSerializer):
	class Meta(TaskSerializer):
		model = TaskPerDay
		fields = TaskSerializer.Meta.fields


class TaskPerWeekSerializer(TaskSerializer):
	class Meta(TaskSerializer):
		model = TaskPerWeek
		fields = TaskSerializer.Meta.fields


class TaskPerMonthSerializer(TaskSerializer):
	class Meta(TaskSerializer):
		model = TaskPerMonth
		fields = TaskSerializer.Meta.fields


class TaskCreateSerializer(serializers.ModelSerializer):
	user = serializers.IntegerField(write_only=True)

	class Meta:
		model = BaseTask
		fields = ('title', 'description', 'user',)


class TaskPerMonthCreateSerializer(serializers.ModelSerializer):
	user = serializers.IntegerField(write_only=True)

	class Meta:
		model = TaskPerMonth
		fields = ('user', 'title', 'description',)

	def create(self, validated_data):
		print(validated_data)
		user_id = validated_data.pop('user')
		user = User.objects.get(id=user_id)
		task = TaskPerMonth.objects.create(title=validated_data['title'],
										   description=validated_data['description'],
										   user=user)
		return task


class TaskPerDayCreateSerializer(serializers.ModelSerializer):
	user = serializers.IntegerField(write_only=True)

	class Meta:
		model = TaskPerMonth
		fields = ('user', 'title', 'description',)

	def create(self, validated_data):
		print(validated_data)
		user_id = validated_data.pop('user')
		user = User.objects.get(id=user_id)
		task = TaskPerDay.objects.create(title=validated_data['title'],
										 description=validated_data['description'],
										 user=user)
		return task


class TaskPerWeekCreateSerializer(serializers.ModelSerializer):
	user = serializers.IntegerField(write_only=True)

	class Meta:
		model = TaskPerMonth
		fields = ('user', 'title', 'description',)

	def create(self, validated_data):
		print(validated_data)
		user_id = validated_data.pop('user')
		user = User.objects.get(id=user_id)
		task = TaskPerWeek.objects.create(title=validated_data['title'],
										  description=validated_data['description'],
										  user=user)
		return task


class ProductSerializers(serializers.ModelSerializer):
	img = serializers.ImageField()

	class Meta:
		model = Product
		fields = ('id','name', 'description', 'price', 'img')


class InventorySerializers(serializers.ModelSerializer):
	# img = serializers.ImageField()
	product = serializers.ReadOnlyField(source='product.name')
	img = serializers.ImageField(source='product.img')
	description = serializers.CharField(source='product.description')

	class Meta:
		model = Inventory
		fields = ('id','product','quantity','img','description')
