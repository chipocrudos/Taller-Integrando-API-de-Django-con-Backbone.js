from django.conf.urls import patterns, url, include
from .views import IndexView
from rest_framework import routers
from .viewSets import (RestaurantViewSet, CategoryViewSet, CityViewSet,
     PaymentViewSet)

router = routers.DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'categorys', CategoryViewSet)
router.register(r'cities', CityViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='inicio'),
    url(r'^api/', include(router.urls)),
)


urlpatterns += patterns('apps.views',
    url(r'^logout/$', 'logout', name='salir'),
)