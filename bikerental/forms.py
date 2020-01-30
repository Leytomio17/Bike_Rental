from django import forms
from bikerental.models import Users


class HomeForm(forms.ModelForm):
    Users = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Users
        fields = ('username', 'password',)
