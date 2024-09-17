from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=20)
    feedback=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name


class Salesorder(models.Model):
    sname=models.CharField(max_length=50)
    productname=models.CharField(max_length=50)
    quantity=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=12)
    secondaryPhonenumber=models.CharField(max_length=12)
    address=models.CharField(max_length=300)
    pincode=models.CharField(max_length=10)
   

class salesdetails(models.Model):
    coustmername=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=50)
    secondaryphonenumber=models.CharField(max_length=50)
    productname=models.CharField(max_length=50)
    quantity=models.CharField(max_length=50)
    deliveryaddress=models.CharField(max_length=200)
    pincode=models.CharField(max_length=10)
    date=models.DateField()


    def __str__(self):
        return self.coustmername

class productsdetails(models.Model):
    prod_name=models.CharField(max_length=70)
    prod_img=models.ImageField(upload_to='pics')
    prod_quantity=models.CharField(max_length=20)
    prod_price=models.IntegerField()
    prod_colour=models.CharField(max_length=20)

    def __str__(self):
        return self.prod_name