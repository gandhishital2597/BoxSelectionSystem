from django.urls import path
from .views import *


urlpatterns = [

    path('products/',ProductListAPIView.as_view(),name='products'),
    path('boxes/',BoxListAPIView.as_view(),name='boxes'),
    path('orders/',OrderListAPIView.as_view(),name='orders'),
    path('orders/<int:order_id>/recommend-box/',BoxRecommendationAPIView.as_view(),name='recommend-box'
    ),
]