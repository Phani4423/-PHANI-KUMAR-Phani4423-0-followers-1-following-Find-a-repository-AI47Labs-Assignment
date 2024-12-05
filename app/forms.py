from django import forms
from app.models import *
class userform(forms.ModelForm):
    class Meta:
        model = User
        fields=['username','password','email']
        widgets = {'password':forms.PasswordInput}
        help_texts={'username':''}
class profileform(forms.ModelForm):
    class Meta:
        model = profile
        fields=['address','pic']