# -*- coding: utf-8 -*-
from django.db import models
from houses.models import House

class Order(models.Model):
    house = models.ForeignKey(House, verbose_name=u'дом', on_delete=models.CASCADE)
    name = models.CharField(u'имя', max_length=50)
    phone = models.CharField(u'телефон', max_length=50)
    date = models.DateField(u'дата', auto_now_add=True)
