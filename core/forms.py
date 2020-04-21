from django import forms 
from django.core.validators import MinValueValidator, MaxValueValidator

class GenerateRandomUserForm(forms.Form):
    total = forms.IntegerField(
        widget = forms.NumberInput(attrs={
            'class':'form-control form-control-lg mr-4 d-flex',
            'placeholder':'Ingrese un numero entre 50 y 500'
        }),
        validators=[
            MinValueValidator(50, message='El minimo debe ser 50'),
            MaxValueValidator(500, message='El minimo debe ser 50')
        ]
    )