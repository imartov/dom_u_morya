# -*- coding: utf-8 -*-
from django import forms
from orders.models import Order
from houses.models import House

class OrderForm(forms.ModelForm):
    personal_data = forms.BooleanField(label=u'Я согласен на обработку персональных данных', required=True)
    house = forms.ModelChoiceField(queryset=House.objects.all(), widget=forms.HiddenInput)
    class Meta:
        model = Order
        fields = ['house', 'name', 'phone']