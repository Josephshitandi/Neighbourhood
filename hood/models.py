
 
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

 
class Neighbourhood(models.Model):
    neighbourhoodName = models.CharField(max_length=250)
    neighbourhoodLocation = models.CharField(max_length=250)
    occupantsCount = models.IntegerField(default=0)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)

