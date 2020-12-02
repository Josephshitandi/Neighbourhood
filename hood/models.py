from django.db import models
from django.contrib.auth.models import User
import cloudinary
from cloudinary.models import CloudinaryField
from tinymce.models import HTMLField
# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    occupantsCount = models.IntegerField(default=0)
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name} neighbourhood'
    
    def save_neighborhood(self):
        self.save()
        
    def delete_neighborhood(self):
        self.delete()
        
class Profile (models.Model):
    name = models.CharField(max_length=30)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    status = models.BooleanField()
    image = models.ImageField('profile pic',default = 'profile.jpg')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    def save_profile(self):
        self.save
    def delete_profile(self):
        self.delete()
        
class Business(models.Model):
    business_name = models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    business_email = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.business_name} business'
    
    def save_business(self):
        self.save()
        
    def delete_business(self):
        self.delete()
        
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,default = '')
    date = models.DateField(auto_now_add=True)
    neighbourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE, default='', null=True, blank=True)
   
    def __str__(self):
        return f'{self.title} Post'
    
    def save_post(self):
        self.save()
        
    def delete_post(self):
        self.delete()