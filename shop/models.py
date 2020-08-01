from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=30, default="")
    category=models.CharField(max_length=50, default="")
    subcategory=models.CharField(max_length=50, default="")
    desc=models.CharField(max_length=300, default="")
    price=models.IntegerField(default=0)
    pub_date =models.DateField()
    image=models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return (self.product_name)

class Transaction(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=30)
    desc=models.CharField(max_length=300)
    amount=models.DecimalField(max_digits=7, decimal_places=2)
class Contact(models.Model):
    msg_id=models.AutoField(primary_key="true")
    name=models.CharField(max_length=30, default="")
    desc=models.CharField(max_length=300, default="")
    email=models.CharField(max_length=50, default="")
    phone=models.DecimalField(max_digits=15, decimal_places=0, default=0)
    def __str__(self):
        return (self.name)
class Checkout(models.Model):
    person_id = models.AutoField(primary_key="true")
    json_order=models.CharField(max_length=5000, default="")
    first_name = models.CharField(max_length=30, default="")
    last_name = models.CharField(max_length=300, default="")
    Address = models.CharField(max_length=300, default="")
    Address_2 = models.CharField(max_length=300, default="")
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")
    zip = models.IntegerField(default=0)
    amount=models.DecimalField(max_digits=100, decimal_places=2,default=0)
    def __str__(self):
        return (self.first_name)

class Orderupdate(models.Model):
    update_id=models.AutoField(primary_key="true")
    order_id=models.IntegerField(default=0)
    updated_desc=models.CharField(max_length=3000, default="")
    first_name=models.CharField(max_length=300, default="")
    time_stamp = models.DateField(auto_now_add=True)
    def __str__(self):
        return (self.updated_desc[0:7]+"....")

class Payment(models.Model):
    pay_id=models.AutoField(primary_key="true")
    person_name=models.CharField(max_length=30, default="")
    image=models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return (self.person_name)