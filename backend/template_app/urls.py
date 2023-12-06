from django.urls import include, path

from .views import IndexView,AboutView,UserTopTableView


urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('about/', AboutView.as_view(), name='about'),
	path('users/', UserTopTableView.as_view(), name='top-users'),

]