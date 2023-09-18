from django import forms

from .models import Product

class AddProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('category','name','description','price','image')
        
        widgets = {
            'category': forms.Select(attrs = {
                'class':'w-full py-4 px-6 rounded-xl border',
                
            }),
            'name':forms.TextInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border',
                'placeholder':'Enter name of the product'
            }),
            'description':forms.Textarea(attrs={
                'class':'w-full py-4 px-6 rounded-xl border',
                'rows':3,'cols':10,
                'placeholder':'Describe the product(optional)'
            }),
            'price':forms.TextInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            }),
            'image':forms.FileInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        }
        
        
class EditProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('name','description','price','image','is_sold')
        
        widgets = {
            'name':forms.TextInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border',
                'placeholder':'Enter name of the product'
            }),
            'description':forms.Textarea(attrs={
                'class':'w-full py-4 px-6 rounded-xl border',
                'rows':3,'cols':10,
                'placeholder':'Describe the product(optional)'
            }),
            'price':forms.TextInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            }),
            'image':forms.FileInput(attrs={
                'class':'w-full py-4 px-6 rounded-xl border'
            })
        }