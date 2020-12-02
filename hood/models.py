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
        
class Profile (models.Model):
    name = models.CharField(max_length=30)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    status = models.BooleanField()
    image = models.ImageField(upload_to = 'profile',default = 'profile.jpg')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    def save_profile(self):
        self.save
    def delete_profile(self):
        self.delete()
        
