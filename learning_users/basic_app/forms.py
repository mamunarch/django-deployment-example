from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

# changing password algorithm & grabbing User's default fields
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

# grabbing additional fields
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
