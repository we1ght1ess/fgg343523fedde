from rest_framework import serializers
from .models import Person, Sex, TreatmentType

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = "__all__"
class SexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sex
        fields = "__all__"

class TreatmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatmentType
        fields = "__all__"

