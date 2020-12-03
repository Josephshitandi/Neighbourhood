# from django.test import TestCase
# from django.contrib.auth.models import User
# from .models import Neighbourhood
# # Create your tests here.

# class NeibourhoodTestClass(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='gee',password='098765')
#         self.location = Location(id=1,name='Test name')
#         self.Neighbourhood = Neighbourhood(id=1,name='Test name',location=self.location,admin=self.user,occupants=1)

#         def test_instance(self):
#             self.assertTrue(isinstance(self.neighbour,Neighbourhood))

#         def test_create_neighbourhood(self):
#             self.location.save()
#             self.neighbourhood.create_neighbourhood()
#             self.assertTrue(len(Neighbourhood.objects.all())>0)

#         def test_delete_neighbourhood(self):
#             self.location.save()
#             self.neighbourhood.create_neighbourhood()
#             self.neighbourhood = Neighbourhood.objects.get(id=1)
#             self.neighbourhood.delete_neighbourhood()
#             self.assertTrue(len(Neighbourhood.objects.all())==0)

#         def test_find_neighbourhood(self):
#             self.location.save()
#             self.neighbourhood.create_neighbourhood()
#             self.searched_neighbourhood = Neighbourhood.find_neighbourhood(1)
#             self.assertTrue(self.searched_neighbourhood==self.neighbourhood)

#         def test_update_neighbourhood(self):
#             self.location.save()
#             self.neighbourhood.create_neighbourhood()
#             self.neighbourhood = Neighbourhood.objects.get(id=1)
#             self.neighbourhood.name = 'Changed name'
#             self. neighbourhood.update_neighbourhood()
#             self.update_neighbourhood = Neighbourhood.objects.get(id=1)
#             self.assertEqual(self.updated_neighbourhood.name,'Changed name')

#         def test_update_occupants(self):
#             self.location.save()
#             self.neighbourhood.create_neighbourhood()
#             self.neighbourhood = Neighbourhood.objects.get(id=1)
#             self.neighbourhood.update_occupants()
#             self.updated_neighbourhood = Neighbourhood.objects.get(id=1)
#             self.assertTrue(self.updated_neighbourhood.occupants ==2)    