from django.urls import include, path
from rest_framework import routers
from .views import TaskPerDayAPIView, TaskPerWeekAPIView, TaskPerMonthAPIView, UsersAPIView, UserProfileAPIView, \
	MarketAPIView, InventoryAPIView, UserSubscribeAPIView, UserUnSubscribeAPIView

# router = routers.SimpleRouter()
# # router.register(r'users', UsersViewSet, basename='User')
urlpatterns = [
	path('users/', UsersAPIView.as_view(), ),
	path('user/<int:pk>/', UserProfileAPIView.as_view(), ),
	path('task-day/', TaskPerDayAPIView.as_view(), ),
	path('task-week/', TaskPerWeekAPIView.as_view(), ),
	path('task-month/', TaskPerMonthAPIView.as_view(), ),
	path('products/', MarketAPIView.as_view(), ),
	path('inventory/', InventoryAPIView.as_view(), ),
	path('subscribe/', UserSubscribeAPIView.as_view(), ),
	path('unsubscribe/', UserUnSubscribeAPIView.as_view(), ),
]
