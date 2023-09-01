from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Merchant,Products
class signupform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
class merchantform(forms.ModelForm):
    class Meta:
        model=Merchant
        fields=['name','surname','city','country','pincode','phoneno','email','shippingadd','billingadd','desc']
class productsform(forms.ModelForm):
    class Meta:
        model=Products
        fields=['product_name','product_desc','category','subcategory','price','product_pub_date','image']