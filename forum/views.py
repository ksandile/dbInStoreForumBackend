from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import tPost
from .serializers import tPostSerializer

class tPostViewSet(viewsets.ModelViewSet):
    queryset = tPost.objects.all()
    serializer_class = tPostSerializer

