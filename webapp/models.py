from django.contrib.auth.models import User,Group
from django.db import models


class distributer(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=12)
    city = models.CharField(max_length=100)
    pincode = models.IntegerField(max_length=6)
    def __str__(self):
        return '{0}'.format(self.name)
    


class contact(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=12)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    def __str__(self):
        return '{0}'.format(self.name)

   

