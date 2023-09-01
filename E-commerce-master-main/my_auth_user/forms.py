from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
class signupform(UserCreationForm):
    
    # Note password fields are not part of below declared signup form .....they are contains of UserCreationForm 
    class Meta:
        # to change the label which is already wrote 
        password2=forms.CharField(label='confirm password(again)',widget=forms.PasswordInput)
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}
        # changing email address to Email 
class EdirUserProfileForm(UserChangeForm):
    password=None # to remove algorithm of password
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined','last_login','is_active']
        labels={'email':'Email'}
        # changing email address to Email 
class EdirAdminProfileForm(UserChangeForm):
    password=None # to remove algorithm of password
    class Meta:
        model=User
        fields='__all__'
        labels={'email':'Email'}
        # changing email address to Email 