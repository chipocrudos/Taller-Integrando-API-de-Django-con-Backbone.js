# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import (Restaurant, Category, City, Payment, Tip)
#from django.core import serializers as serialization


class RestaurantSerializer(serializers.ModelSerializer):
    tips = serializers.SerializerMethodField('_get_tips')
    thum = serializers.SerializerMethodField('_get_thum')
    cities = serializers.SerializerMethodField('_get_cities')

    def _get_tips(self, restaurant):
        return restaurant.tip_set.count()

    def _get_thum(self, restaurant):
        return restaurant.imagen.url_200x200

    def _get_cities(self, restaurant):
        city = City.objects.filter(establishment__restaurant=restaurant)
        #return serialization.serialize('json', city)
        return city

    class Meta:
        model = Restaurant
        #fields = ('establishment_set',)
        #exclude = ('payment', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip