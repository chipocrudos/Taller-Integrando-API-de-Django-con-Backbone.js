# -*- coding: utf-8 -*-
import django_filters
from .models import Restaurant


class RestaurantFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(name='category__name')
    payment = django_filters.CharFilter(name='payment__pay')

    class Meta:
        model = Restaurant
        fields = ('name', 'description', 'category', 'payment',)