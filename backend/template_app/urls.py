from django.urls import include, path

from .views import IndexView, AboutView, UserTopTableView, UserProfilView, ProductListView, TaskСompletedView, \
	TaskDeletedView, InventoryView, InventoryDeleteView, ProductBayView, UserRegisterView, UserLoginView

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('about/', AboutView.as_view(), name='about'),
	path('users/', UserTopTableView.as_view(), name='top-users'),
	path('user/<int:pk>/', UserProfilView.as_view(), name='user'),
	path('market/', ProductListView.as_view(), name='market'),
	path('task-complited/<int:pk>/<slug:type>/', TaskСompletedView.as_view(), name='taskcompleted'),
	path('task-deleted/<int:pk>/<slug:type>/', TaskDeletedView.as_view(), name='taskdelete'),
	path('inventory/', InventoryView.as_view(), name='inventory'),
	path('inventory-bay/<int:pk>/', ProductBayView.as_view(), name='inventory-bay'),
	path('inventory-deleted/', InventoryDeleteView.as_view(), name='inventory-delete'),
	path('register/', UserRegisterView.as_view(), name='register'),
	path('login/', UserLoginView.as_view(), name='login'),

]
