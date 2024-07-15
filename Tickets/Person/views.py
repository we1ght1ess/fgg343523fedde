from rest_framework import generics
from django.shortcuts import render
from .models import Person, Sex, TreatmentType
from .serializers import PersonSerializer, SexSerializer, TreatmentTypeSerializer
class PersonAPIView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class SexAPIView(generics.ListCreateAPIView):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer

class SexAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sex.objects.all()
    serializer_class = SexSerializer

class TreatmentTypeAPIView(generics.ListCreateAPIView):
    queryset = TreatmentType.objects.all()
    serializer_class = TreatmentTypeSerializer

class TreatmentTypeAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TreatmentType.objects.all()
    serializer_class = TreatmentTypeSerializer