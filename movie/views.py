from django.shortcuts import render
from .models import Movidata
from .serializers import MoviSerializer
from rest_framework import viewsets
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movidata.objects.all()
    serializer_class = MoviSerializer