from django import forms
from .models import UserData

class UserdataForm(forms.ModelForm):

    class Meta:
        model = UserData
        fields = ('uid', 'first_name', 'last_name', 'latitude', 'longitude')
        labels = {"uid":"UID"}

class UpdateForm(forms.Form):
    uid = forms.CharField()
