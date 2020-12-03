from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import NeighbourhoodSerializer
from rest_framework import status
from django.http import HttpResponse, Http404, HttpResponseRedirect
from rest_framework import viewsets
from .models import Neighborhood
# Create your views here.



class NeighbourhoodViewSet(viewsets.ModelViewSet):
    queryset = Neighbourhood.objects.all()
    serializer_class = NeighbourhoodSerializer