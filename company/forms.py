from django import forms
from django.contrib.auth.models import User
from .models import UploadedFile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file'] 

class QueryBuilderForm(forms.Form):
    keyword = forms.CharField(required=False)
    industry = forms.CharField(required=False)
    year_founded = forms.IntegerField(required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    country = forms.CharField(required=False)
    employees_from = forms.IntegerField(required=False)
    employees_to = forms.IntegerField(required=False)