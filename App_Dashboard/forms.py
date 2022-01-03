from django import forms
from App_Dashboard.models import Country, DesignerInfo, Post, Reply


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = '__all__'


class DesignerInfoForm(forms.ModelForm):
    class Meta:
        model = DesignerInfo
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description',]


class ReplyFrom(forms.ModelForm):
    class Meta:
        model = Reply
        fields = '__all__'
