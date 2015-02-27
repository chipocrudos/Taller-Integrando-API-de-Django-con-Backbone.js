from django.db import models
from django.contrib.auth.models import User
from django_thumbs.db.models import ImageWithThumbsField


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Payment(models.Model):
    pay = models.CharField(max_length=50)

    def __unicode__(self):
        return self.pay


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    payment = models.ManyToManyField(Payment)
    category = models.ManyToManyField(Category)
    description = models.TextField()
    #imagen = models.ImageField(upload_to='fotos')
    imagen = ImageWithThumbsField(upload_to='fotos', sizes=((125, 125),
(200, 200)))

    def __unicode__(self):
        return self.name


class Establishment(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    city = models.ForeignKey(City)
    address = models.CharField(max_length=50)

    def __unicode__(self):
        return self.address


class Tip(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    user = models.ForeignKey(User)
    content = models.TextField(max_length=200)

    def __unicode__(self):
        return self.content