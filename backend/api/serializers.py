from rest_framework import serializers

from users.models import User, Subscribe


class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'username', 'first_name', 'last_name', 'email', 'balance', 'points','rank')

# def get_is_subscribed(self, obj):
# 	request_user = self.context.get('request_user', None).id
# 	followers = Subscribe.objects.filter(user=request_user, author=obj).exists()
# 	return followers
