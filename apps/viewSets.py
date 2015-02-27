# -*- coding: utf-8 -*-
from rest_framework import viewsets
from rest_framework.decorators import link
from rest_framework.response import Response
from rest_framework.filters import DjangoFilterBackend
from .models import (Restaurant, Category, City, Payment)
from .serializer import (RestaurantSerializer, CategorySerializer,
     CitySerializer, PaymentSerializer, TipSerializer)
from .filters import RestaurantFilter


class RestaurantViewSet(viewsets.ReadOnlyModelViewSet):
    model = Restaurant
    serializer_class = RestaurantSerializer
    paginate_by = 5
    queryset = Restaurant.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = RestaurantFilter

    @link()
    def tips(self, request, pk=None):
        restaurant = self.get_object()
        tips = restaurant.tip_set.all()
        serializer = TipSerializer(tips, many=True)
        return Response(serializer.data)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    model = Category
    serializer_class = CategorySerializer

    @link()
    def restaurants(self, request, pk=None):
        category = self.get_object()
        restaurants = category.restaurant_set.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)


class CityViewSet(viewsets.ReadOnlyModelViewSet):
    model = City
    serializer_class = CitySerializer

    @link()
    def restaurants(self, request, pk=None):
        restaurants = Restaurant.objects.filter(establishment__city__pk=pk)
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    @link()
    def payments(self, request, pk=None):
        restaurants = Restaurant.objects.filter(establishment__city__pk=pk)
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)


class PaymentViewSet(viewsets.ReadOnlyModelViewSet):
    model = Payment
    serializer_class = PaymentSerializer

    @link()
    def restaurants(self, request, pk=None):
        payment = self.get_object()
        restaurants = payment.restaurant_set.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)