from django import forms
from .models import Items, Accessories

#Form to add Item
class ItemRegister(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['image','name', 'price', 'quantity', 'brand']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
#form to update items
class UpdateItems(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['image','name', 'price', 'quantity', 'brand']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
# Form to add Accessories
class AccessoriesRegistration(forms.ModelForm):
    class Meta:
        model = Accessories
        fields = ['image','name', 'price', 'quantity', 'brand']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
        }

#form to update Accessories
class UpdateAccessories(forms.ModelForm):
    class Meta:
        model = Accessories
        fields = ['image','name', 'price', 'quantity', 'brand']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
        }