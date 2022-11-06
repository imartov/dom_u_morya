# -*- coding: utf-8 -*-
from django import forms

class HousesFilterForm(forms.Form):
    min_price = forms.IntegerField(label=u'от', required=False)
    max_price = forms.IntegerField(label=u'до', required=False)
    query = forms.CharField(label=u'описание', required=False)
    ordering = forms.ChoiceField(label=u'сортировка', required=False, choices=[
        ('name', u'по алфавиту'),
        ('price', u'дешевые сверху'),
        ('-price', u'дорогие сверху')
    ])
