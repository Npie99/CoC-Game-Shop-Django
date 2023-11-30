from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class productPS5(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    picture = models.ImageField(upload_to="productPS5", null=True, blank=True)
    specfile = models.FileField(upload_to="specfilePS5", null=True, blank=True)

    def __str__(self):
        return self.title
    
class productPS4(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    picture = models.ImageField(upload_to="productPS4", null=True, blank=True)
    specfile = models.FileField(upload_to="specfilePS4", null=True, blank=True)

    def __str__(self):
        return self.title
    
class productNintendo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    picture = models.ImageField(upload_to="productNS", null=True, blank=True)
    specfile = models.FileField(upload_to="specfileNS", null=True, blank=True)

    def __str__(self):
        return self.title
    
class contactList(models.Model):
    topic = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    detail = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.topic
    
class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    usertype = models.CharField(max_length=100, default='member')
    point = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    
class action(models.Model):
    contactList = models.ForeignKey(contactList, on_delete=models.CASCADE)
    actionDetail = models.TextField()

    def __str__(self):
        return self.contactList.topic
    
class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)

