from rest_framework.generics import RetrieveAPIView, ListAPIView

from orders.models import Order
from orders.serializers import OrderSerializer, OrderDetailsSerializer


class OrderRetrieveView(RetrieveAPIView):
    serializer_class = OrderDetailsSerializer
    queryset = Order.objects.select_related(
        'order_payment',
        'billing_address',
        'tracking_informations',
    ).prefetch_related(
        'products',
    ).all()


class OrderListView(ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
