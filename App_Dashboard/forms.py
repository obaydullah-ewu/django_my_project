from django import forms
from App_Dashboard.models import Country


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'