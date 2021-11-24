from django import forms
from App_Dashboard.models import Country, DesignerInfo


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'


class DesignerInfoForm(forms.ModelForm):
    class Meta:
        model = DesignerInfo
        fields = '__all__'