from django import forms
from .models import *

class ItemForm(forms.ModelForm):
    
    class Meta:
        model = Item
        fields = ('title', 'price', 'discount_price', 'category', 'slug', 'description', 'image', )
        
