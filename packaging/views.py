from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Box, Order
from .serializers import (
    ProductSerializer,
    BoxSerializer,
    OrderSerializer
)

from .services import recommend_box


class ProductListAPIView(APIView):

    def get(self, request):

        products = Product.objects.all()

        serializer = ProductSerializer(
            products,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        serializer = ProductSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class BoxListAPIView(APIView):

    def get(self, request):

        boxes = Box.objects.all()

        serializer = BoxSerializer(
            boxes,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        serializer = BoxSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class OrderListAPIView(APIView):

    def get(self, request):

        orders = Order.objects.all()

        serializer = OrderSerializer(
            orders,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        serializer = OrderSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class BoxRecommendationAPIView(APIView):

    def get(self, request, order_id):

        try:

            order = Order.objects.get(
                id=order_id
            )

        except Order.DoesNotExist:

            return Response(
                {
                    "error": "Order not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        box = recommend_box(order)

        if box is None:

            return Response(
                {
                    "message": "No suitable box found"
                },
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            {
                "order_id": order.id,

                "recommended_box": {
                    "id": box.id,
                    "name": box.name,

                    "dimensions": {
                        "length": box.length,
                        "width": box.width,
                        "height": box.height
                    },

                    "max_weight": box.max_weight,
                    "cost": float(box.cost)
                }
            },

            status=status.HTTP_200_OK
        )