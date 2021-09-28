from django.core.validators import MinValueValidator
from django import forms

class EntryForm(forms.Form):
    name = forms.CharField(label='Product', max_length=100)
    amount = forms.IntegerField(label='Amount')
    price = forms.FloatField(label='Price', validators=[MinValueValidator(0.0)])
    note = forms.CharField(label="Note", max_length=200)