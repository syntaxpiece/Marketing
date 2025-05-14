from django import forms
from django.contrib.auth.models import User
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductSale
        fields = ['cridet', 'status']
        widgets = {
            'cridet': forms.TextInput(attrs={
                'placeholder': 'Credit',
                'class': 'form-control custom-input m-3'
            }),
        }



class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseSale
        fields = ['cridet', 'status']
        widgets = {
            'cridet': forms.TextInput(attrs={
                'placeholder': 'Credit',
                'class': 'form-control custom-input m-3'
            }),
        }


class ConsultationForm(forms.ModelForm):
    class Meta:
        model = ConsultationSale
        fields = ['cridet', 'status']
        widgets = {
            'cridet': forms.TextInput(attrs={
                'placeholder': 'Credit',
                'class': 'form-control custom-input m-3'
            }),
        }