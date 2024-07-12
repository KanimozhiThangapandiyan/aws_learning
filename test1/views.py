from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Country
from .serializers import CountrySerializer

def home(request):
    return HttpResponse("kani")

class CountryListCreateView(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CountryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer