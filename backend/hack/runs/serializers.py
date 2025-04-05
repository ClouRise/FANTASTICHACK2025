from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    color = serializers.CharField(read_only=True)
    
    class Meta:
        model = Person
        fields = ['color']
