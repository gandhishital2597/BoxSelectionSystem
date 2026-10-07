#
# from rest_framework import serializers
# from .models import Product, Box, Order, OrderItem
#
# class ProductSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Product
#         fields = '__all__'
#
#
# class BoxSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Box
#         fields = '__all__'
#
#
# class OrderItemSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = OrderItem
#         fields = '__all__'
#
#
# class OrderSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Order
#         fields = '__all__'

#update serializers for validation
from rest_framework import serializers

from .models import Product, Box, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

    def validate_length(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Length must be greater than 0."
            )

        return value

    def validate_width(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Width must be greater than 0."
            )

        return value

    def validate_height(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Height must be greater than 0."
            )

        return value

    def validate_weight(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Weight must be greater than 0."
            )

        return value


class BoxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Box
        fields = '__all__'

    def validate_length(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Length must be greater than 0."
            )

        return value

    def validate_width(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Width must be greater than 0."
            )

        return value

    def validate_height(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Height must be greater than 0."
            )

        return value

    def validate_max_weight(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Maximum weight must be greater than 0."
            )

        return value

    def validate_cost(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Cost must be greater than 0."
            )

        return value


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'