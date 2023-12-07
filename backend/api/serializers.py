import json

from djoser.serializers import UserSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from todolist_app.models import TaskPerDay, BaseTask, TaskPerWeek, TaskPerMonth
from users.models import User, Subscribe


class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'first_name', 'last_name', 'email', 'balance', 'points', 'rank')


# def get_is_subscribed(self, obj):
# 	request_user = self.context.get('request_user', None).id
# 	followers = Subscribe.objects.filter(user=request_user, author=obj).exists()
# 	return followers

class TaskSerializer(serializers.ModelSerializer):
	class Meta:
		model = BaseTask
		fields = ('title', 'description', 'is_completed',)


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
		fields = ('title', 'description', 'user')


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
