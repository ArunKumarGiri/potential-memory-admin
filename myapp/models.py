from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

# Create your models here.
# class NormalUser(models.Model):
#     name = models.CharField(max_length = 150,default="")
#     employee_id  = models.IntegerField()
#     description = models.TextField()
    
#     def __str__(self):
#     	return self.name

    
# class MainUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length = 150,default="")
#     emp_no  = models.IntegerField(default="")
#     description = models.TextField()    
    
    
#     def __str__(self):
#     	return self.name


class Notes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(default="",max_length=1000)
    description=models.TextField(default="")
    when_add=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name




user_type=(('1','normal_user'),('2','employee_user'))

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)
    address = models.TextField()
    user_type = models.CharField(max_length=20,choices=user_type)
    Date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.user)

