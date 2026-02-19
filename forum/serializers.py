from rest_framework import serializers
from .models import tPost

class tPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = tPost
        fields = '__all__'
