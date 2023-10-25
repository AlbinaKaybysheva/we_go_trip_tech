import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser


from .models import Product, Order, Payment
from .serializers import ProductSerializer
from .constants import *



@api_view(['GET'])
def get_product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_order(request):
    data = JSONParser().parse(request)
    product_ids = [el["id"] for el in data.get("products")]
    amount = sum(Product.objects.filter(pk__in=product_ids).values_list('price', flat=True))
    order = Order(amount=amount, created_at=datetime.datetime.now())
    order.save()
    order.products.add(*product_ids)
    return Response({"order_id": order.id}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def create_payment(request):
    data = JSONParser().parse(request)
    order_id = data.get('order_id', None)
    if order_id is None:
        return Response({"error": "Order ID is required."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        order = Order.objects.get(pk=order_id)
        payment = Payment(amount=order.amount, payment_type=data.get('payment_type', payment_type_cash), order=order)
        payment.save()
        return Response({"payment_id": payment.id}, status=status.HTTP_201_CREATED)
    except Order.DoesNotExist:
        return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)
