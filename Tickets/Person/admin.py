from django.contrib import admin
from .models import Sex, Person, TreatmentType

@admin.register(Sex)
class SexAdmin(admin.ModelAdmin):
    list_display = ('SexTitleFull', 'SexTitleShort', 'IsActive')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('PersonFirstName', 'PersonSecondName', 'PersonLastName', 'PersonDataBirth',
                    'TreatmentTypeID', 'SexID', 'IsActive')

@admin.register(TreatmentType)
class TreatmentTypeAdmin(admin.ModelAdmin):
    list_display = ('TreatmentTypeTitle', 'IsActive')
