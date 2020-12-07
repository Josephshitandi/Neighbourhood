
 
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

 class Business(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default = '')
    email = models.CharField(max_length=100, default = '')
    neighbourhood = models.ForeignKey("Neighbourhood",on_delete=models.CASCADE, default='', null=True, blank=True)
    description = models.TextField( default = '')



    def __str__(self):
        return f'{self.name} business'


    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()