
from rest_framework import serializers
from .models import *
        
class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('id', 'name', 'user', 'email', 'neighbourhood', 'description')


class BusinessSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    neighbourhood = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model =  Business
        fields = ['businessName', 'user', 'neighbourhood', 'businessEmail']  
        
        

