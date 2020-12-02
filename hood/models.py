from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Neighbourhood(models.Model):
    hoodName = models.CharField(max_length=250)
    hoodLocation = models.CharField(max_length=250)
    occupantsCount = models.IntegerField(default=0)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.hoodName} neighbourhood'
    def save_neighborhood(self):
        self.save()
    def delete_neighborhood(self):
        self.delete()
