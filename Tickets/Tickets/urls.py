"""
URL configuration for Tickets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Documents.views import DocumentsAPIView, DocumentsAPIDetailView, DocumentTypeAPIView, DocumentTypeAPIDetailView, \
        DocumentCategoryAPIView, DocumentCategoryAPIDetailView, PersonDocumentAPIView, PersonDocumentAPIDetailView
from Person.views import PersonAPIView, PersonAPIDetailView, SexAPIView, SexAPIDetailView, TreatmentTypeAPIView, \
        TreatmentTypeAPIDetailView
urlpatterns = [
    path('admin/', admin.site.urls),

path('api/v1/DocumentList/', DocumentsAPIView.as_view()),
    path('api/v1/DocumentList/<int:pk>/', DocumentsAPIView.as_view()),
    path('api/v1/DocumentListDetail/<int:pk>/', DocumentsAPIDetailView.as_view()),

    path('api/v1/DocumentTypeList/', DocumentTypeAPIView.as_view()),
    path('api/v1/DocumentTypeList/<int:pk>/', DocumentTypeAPIView.as_view()),
    path('api/v1/DocumentListDetail/<int:pk>/', DocumentTypeAPIDetailView.as_view()),

    path('api/v1/DocumentCategoryList/', DocumentCategoryAPIView.as_view()),
    path('api/v1/DocumentCategoryList/<int:pk>/', DocumentCategoryAPIView.as_view()),
    path('api/v1/DocumentCategoryDetail/<int:pk>/', DocumentCategoryAPIDetailView.as_view()),

    path('api/v1/PersonDocumentList/', PersonDocumentAPIView.as_view()),
    path('api/v1/PersonDocumentList/<int:pk>/', PersonDocumentAPIView.as_view()),
    path('api/v1/PersonDocumentDetail/<int:pk>/', PersonDocumentAPIDetailView.as_view()),

    path('api/v1/PersonList/', PersonAPIView.as_view()),
    path('api/v1/PersonList/<int:pk>/', PersonAPIView.as_view()),
    path('api/v1/PersonDetail/<int:pk>/', PersonAPIDetailView.as_view()),

    path('api/v1/SexList/', SexAPIView.as_view()),
    path('api/v1/SexList/<int:pk>/', SexAPIView.as_view()),
    path('api/v1/SexDetail/<int:pk>/', SexAPIDetailView.as_view()),

    path('api/v1/TreatmentTypeList/', TreatmentTypeAPIView.as_view()),
    path('api/v1/TreatmentTypeList/<int:pk>/', TreatmentTypeAPIView.as_view()),
    path('api/v1/TreatmentTypeDetail/<int:pk>/', TreatmentTypeAPIDetailView.as_view()),
]
