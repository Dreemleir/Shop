from django import forms 
from .models import *
  
"""class HotelForm(forms.ModelForm): 
  
    class Meta: 
        model = Hotel 
        fields = ['name', 'hotel_Main_Img'] """

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'price', 'size', 'currency', 'imageURL']