from django.urls import path

from orders.views import OrderRetrieveView, OrderListView


urlpatterns = [
    path('<str:pk>', OrderRetrieveView.as_view(), name='order'),
    path('', OrderListView.as_view(), name='order-list'),
]