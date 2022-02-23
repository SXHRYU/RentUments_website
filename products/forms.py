from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='', 
                    widget=forms.TextInput(
                        attrs={"placeholder": "Your title"}
                        )
                    )
    description = forms.CharField(widget=forms.Textarea(
                    attrs={'rows': 10, 
                            'maxlength': 100, 
                            'placeholder': 'max length = 100'}
                            ))
    email       = forms.EmailField()
    class Meta:
        model = Product
        fields = [
            'title', 
            'description', 
            'price',
            'email',
        ]
    
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not 'CFE' in title:
            raise forms.ValidationError('This is not a valid title')
        return title

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('edu'):
            raise forms.ValidationError('This is not a valid email')

class RawProductForm(forms.Form):
    title       = forms.CharField()
    description = forms.CharField()
    price       = forms.DecimalField()
    featured    = forms.BooleanField(required=False)