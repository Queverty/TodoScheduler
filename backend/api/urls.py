from django.urls import include, path
from rest_framework import routers
from .views import UsersViewSet, TaskPerDayView, TaskPerWeekView, TaskPerMonthView

router = routers.SimpleRouter()
router.register(r'users', UsersViewSet, basename='User')
urlpatterns = [
	path('', include(router.urls)),
	path('task-day/', TaskPerDayView.as_view(), ),
	path('task-week/', TaskPerWeekView.as_view(), ),
	path('task-month/', TaskPerMonthView.as_view(), ),
]
