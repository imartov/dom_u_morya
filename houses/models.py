# -*- coding: utf-8 -*-
from django.db import models

class House(models.Model):
    name = models.CharField(u'название', max_length=50)
    price = models.IntegerField(u'цена')
    description = models.TextField(u'описание')
    photo = models.ImageField(u'фотография', upload_to='houses/photos', default='', blank=True)
    active = models.BooleanField(u'активен', default=True)

    class Meta:
        verbose_name = u'дом'
        verbose_name_plural = u'дома'
        ordering = ['-active', 'name']

    def __str__(self):
        return self.name
