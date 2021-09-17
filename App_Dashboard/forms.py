from django import forms
from App_Dashboard.models import Country, TaxiCompany


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'


class TaxiCompanyForm(forms.ModelForm):
    class Meta:
        model = TaxiCompany
        fields = '__all__'