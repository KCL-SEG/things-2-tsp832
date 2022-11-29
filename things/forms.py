"""Forms of the project."""

from .models import Thing
from django import forms

# Create your forms here.
class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea()}

    # name = forms.CharField(label = 'Name', max_length=35)
    # description = forms.CharField(label = 'Description', widget = forms.Textarea())
    # quantity = forms.IntegerField(label = 'Quantity')
