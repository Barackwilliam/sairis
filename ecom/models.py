from django.db import models
from django.utils import timezone


# Hosting settings
from django.utils.timezone import now, timedelta
from django.contrib import admin
from django.utils.timezone import now
from datetime import timedelta



from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= CloudinaryField('image')
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Product(models.Model):
    name=models.CharField(max_length=80)
    product_image= CloudinaryField('image')
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=500)
    def __str__(self):
        return self.name
    

class Product_1(models.Model):
    name=models.CharField(max_length=80)
    product_image= CloudinaryField('image')
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=500)
    def __str__(self):
        return self.name
    
class Product_2(models.Model):
    name=models.CharField(max_length=80)
    product_image= CloudinaryField('image')
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=500)
    def __str__(self):
        return self.name
    

   
class Product_3(models.Model):
    name=models.CharField(max_length=80)
    product_image= CloudinaryField('image')
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=500)
    def __str__(self):
        return self.name
    


class Product_4(models.Model):
    name=models.CharField(max_length=80)
    product_image= CloudinaryField('image')
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=500)
    def __str__(self):
        return self.name





class Product_5(models.Model):
    name=models.CharField(max_length=80)
    product_image= CloudinaryField('image')
    price = models.PositiveIntegerField()
    description=models.CharField(max_length=500)
    def __str__(self):
        return self.name



class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)


class Feedback(models.Model):
    name=models.CharField(max_length=40)
    feedback=models.CharField(max_length=500)
    date= models.DateField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name




# hosting settings


from django.utils.timezone import now
from datetime import timedelta

# Function to return the default expiration date
def default_expiration_date():
    return now() + timedelta(days=30)

class HostingStatus(models.Model):
    is_active = models.BooleanField(default=True)
    expiration_date = models.DateTimeField(default=default_expiration_date)

    def time_remaining(self):
        remaining = self.expiration_date - now()
        return remaining if remaining.total_seconds() > 0 else timedelta(seconds=0)

    def is_expired(self):
        return self.time_remaining().total_seconds() <= 0

    def __str__(self):
        return "Hosting Status"