from rest_framework import serializers
from .models import DocumentCategory, Document, DocumentType, PersonDocument

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"
class DocumentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentCategory
        fields = "__all__"

class DocumentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = "__all__"

class PersonDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonDocument
        fields = "__all__"