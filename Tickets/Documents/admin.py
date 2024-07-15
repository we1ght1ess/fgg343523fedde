from django.contrib import admin
from .models import DocumentCategory, Document, DocumentType, PersonDocument

@admin.register(DocumentCategory)
class DocumentCategoryAdmin(admin.ModelAdmin):
    list_display = ('DocumentCategoryTitle', 'DocumentCategoryNotes', 'IsActive')

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('DocumentTypeID','DocumentSeries','DocumentNumber','DocumentNumberAdditional', 'DocumentDateIssue',
                    'DocumentIssuerOfficial', 'DocumentIssuerAdditionalNotes', 'DocumentDateExpire', 'IsActive')

@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('DocumentTypeTitleFull', 'DocumentTypeTitleShort', 'DocumentTypeNotes', 'DocumentCategoryID',
                    'CountryID', 'IsActive')

@admin.register(PersonDocument)
class DocumentCategoryAdmin(admin.ModelAdmin):
    list_display = ('PersonID', 'DocumentID', 'PersonDocumentDateInput', 'InputDataNotes', 'IsActive')