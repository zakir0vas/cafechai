
from django.urls import path
from . import views

urlpatterns = [
    path('register/admin/', views.AdministratorRegistrationView.as_view(), name='admin-registration'),
    path('register/client/', views.ClientRegistrationView.as_view(), name='client-registration'),
    path('menu/', views.MenuListView.as_view(), name='menu-list'),
    path('menu/<int:pk>/', views.MenuItemDetailView.as_view(), name='menu-detail'),
    path('orders/', views.OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
]
