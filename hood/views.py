from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from .serializer import *
from rest_framework import status

def home(request):
    hood = Neighbourhood.objects.all()
    business = Business.objects.all()
    posts = Post.objects.all()
    print("Results..", posts)
      
    return render(request, "home.html", {"hoods":hood, "business":business,"posts":posts})
class NeighbourhoodViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing neighborhood instances.
    """
    serializer_class = NeighbourhoodSerializer
    queryset = Neighbourhood.objects.all()
    
class ProfileViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing profile instances.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
class BusinessViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing profile instances.
    """
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()

class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing profile instances.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()