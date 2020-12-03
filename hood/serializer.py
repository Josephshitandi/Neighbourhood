from rest_framework import serializers
from .models import Neighbourhood


class NeighbourhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighbourhood
        # fields = ('neighbourhood_name','location','occupants')
        fields = __All__
