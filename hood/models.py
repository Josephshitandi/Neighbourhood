from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Neighbourhood(models.Models)
    neighbourhood_name = models.CharField(max_lenght=50)
    location = models.ForeignKey('Location',on_delete = models.CASCADE,null = True)
    admin = models.ForeignKey(User,on_delete = models.CASCADE)
    occupants = models.IntegerField(null=True)

    def __str__(self):
      return self.neighbourhood_name

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def find_neighbourhood(cls,neighbourhood_id):
        neighbourhood = cls.objects.get(id = neighbourhood_id)
        return neighbourhood

        def update_neighbourhood(self):
            self.save()

        def update_occupants(self):
            self.occupants +=1
            self.save()
