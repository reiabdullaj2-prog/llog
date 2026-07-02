from django import forms
from .models import fitimet, shpenzimet
class fitimetForm(forms.ModelForm):
    class Meta:
        model = fitimet
        fields = ['kategoria', 'data', 'shuma']
        widgets = {'kategoria': forms.TextInput(attrs={'class': 'form-control'}),'shuma': forms.NumberInput(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'type': 'date'}),
        }

class shpenzimetForm(forms.ModelForm):
    class Meta:
        model = shpenzimet
        fields = ['kategoria', 'data', 'shuma']
        widgets = {'kategoria': forms.TextInput(attrs={'class': 'form-control'}),'shuma': forms.NumberInput(attrs={'class': 'form-control'}),
            'data': forms.DateInput(attrs={'type': 'date'}),
        }