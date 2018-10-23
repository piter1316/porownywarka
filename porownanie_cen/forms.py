

from django import forms
from . import models



class CreateBrand(forms.ModelForm):
    nazwa = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Nazwa Brandu',
               }
    ))

    class Meta:
        model = models.Brand
        fields = ['nazwa', 'logo']


class UpdateBrand(CreateBrand):
    class Meta:
        model = models.Brand
        fields = ['nazwa', 'logo']
