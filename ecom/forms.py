from django import forms
from django.contrib.auth.models import User
from . import models


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile','profile_pic']

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['name','price','description','product_image']



class ProductForm_1(forms.ModelForm):
    class Meta:
        model=models.Product_1
        fields=['name','price','description','product_image']



class ProductForm_2(forms.ModelForm):
    class Meta:
        model=models.Product_2
        fields=['name','price','description','product_image']



class ProductForm_3(forms.ModelForm):
    class Meta:
        model=models.Product_3
        fields=['name','price','description','product_image']



class ProductForm_4(forms.ModelForm):
    class Meta:
        model=models.Product_4
        fields=['name','price','description','product_image']



class ProductForm_5(forms.ModelForm):
    class Meta:
        model=models.Product_5
        fields=['name','price','description','product_image']


#address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['name','feedback']

#for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Orders
        fields=['status']

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
