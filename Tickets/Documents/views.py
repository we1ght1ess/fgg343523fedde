from rest_framework import generics
from django.shortcuts import render
from .models import Document, DocumentType, DocumentCategory, PersonDocument
from .serializers import DocumentsSerializer, DocumentTypeSerializer, DocumentCategorySerializer, \
    PersonDocumentSerializer

class DocumentsAPIView(generics.ListCreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentsSerializer

class DocumentsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentsSerializer

class DocumentTypeAPIView(generics.ListCreateAPIView):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer

class DocumentTypeAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypeSerializer

class DocumentCategoryAPIView(generics.ListCreateAPIView):
    queryset = DocumentCategory.objects.all()
    serializer_class = DocumentCategorySerializer

class DocumentCategoryAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DocumentCategory.objects.all()
    serializer_class = DocumentCategorySerializer

class PersonDocumentAPIView(generics.ListCreateAPIView):
    queryset = PersonDocument.objects.all()
    serializer_class = PersonDocumentSerializer

class PersonDocumentAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PersonDocument.objects.all()
    serializer_class = PersonDocumentSerializer