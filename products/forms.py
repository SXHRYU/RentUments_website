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
    class Meta:
        model = Product
        fields = [
            'title', 
            'description', 
            'price',
            'featured',
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not 'CFE' in title:
            raise forms.ValidationError('This is not a valid title')
        return title

class RawProductForm(forms.Form):
    title       = forms.CharField()
    description = forms.CharField()
    price       = forms.DecimalField()
    featured    = forms.BooleanField(required=False)