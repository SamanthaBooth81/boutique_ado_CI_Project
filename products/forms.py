"""Product Form for Super User"""
from django import forms
from .models import Products, Category


class ProductForm(forms.ModelForm):
    """Product Form class for super user to upload products"""
    class Meta:
        """Form Metadata"""
        model = Products
        fields = '__all__'  # will include all fields

    def __init__(self, *args, **kwargs):
        """Override init method to change the categories
        to show their friendly names"""
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # List comprehension - short hand for loop
        friendly_names = [(
            c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
