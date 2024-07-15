from django.db import models

class DocumentCategory(models.Model):
    DocumentCategoryTitle = models.CharField(verbose_name='Название категории документа', max_length=100, blank=False)
    DocumentCategoryNotes = models.CharField(verbose_name='Примечания для категории документа', max_length=500, blank=False)
    IsActive = models.BooleanField(verbose_name='Активный', default=True)

    class Meta:
        verbose_name = 'Категория документа'
        verbose_name_plural = 'Категории документов'

    def __str__(self):
        return f'{self.DocumentCategoryTitle}'

class DocumentType(models.Model):
    DocumentTypeTitleFull = models.CharField(verbose_name='Полное название типа документа', max_length=100, blank=False)
    DocumentTypeTitleShort = models.CharField(verbose_name='Короткое название типа документа', max_length=20, blank=False)
    DocumentTypeNotes = models.CharField(verbose_name='Примечания для типа документа', max_length=500, blank=False)
    DocumentCategoryID = models.ForeignKey(DocumentCategory, verbose_name='Категория документа', on_delete=models.CASCADE, blank=False)
    CountryID = models.IntegerField(verbose_name='Страна', blank=False)
    IsActive = models.BooleanField(verbose_name='Активный', default=True)

    class Meta:
        verbose_name = 'Тип документа'
        verbose_name_plural = 'Типы документов'

    def __str__(self):
        return f'{self.DocumentTypeTitleFull}'

class PersonDocument(models.Model):
    PersonID = models.IntegerField(verbose_name='Человек', blank=False)
    DocumentID = models.ForeignKey('Document', verbose_name='Тип документа', on_delete=models.CASCADE, blank=False)
    PersonDocumentDateInput = models.DateField(verbose_name='Дата составления документа', blank=False)
    InputDataNotes = models.CharField(verbose_name='Примечания даты составления', max_length=500, blank=False)
    IsActive = models.BooleanField(verbose_name='Активный', default=True)

    class Meta:
        verbose_name = 'Документ подтверждающий личность'
        verbose_name_plural = 'Документы подтверждающие личность'

    def __str__(self):
        return f'{self.PersonID}'

class Document(models.Model):
    DocumentTypeID = models.ForeignKey(DocumentType, verbose_name='Номер типа документа', on_delete=models.CASCADE, blank=False)
    DocumentSeries = models.CharField(verbose_name='Серия документа', max_length=100, blank=False)
    DocumentNumber = models.CharField(verbose_name='Номер документа', max_length=100, blank=False)
    DocumentNumberAdditional = models.CharField(verbose_name='Дополнительный номер документа', max_length=100, blank=False)
    DocumentDateIssue = models.DateField(verbose_name='Дата выдачи документа', blank=False)
    DocumentIssuerOfficial = models.CharField(verbose_name='Официальный эмитент документа', max_length=200, blank=False)
    DocumentIssuerAdditionalNotes = models.CharField(verbose_name='Дополнительная информация о документе', max_length=200, blank=False)
    DocumentDateExpire = models.DateField(verbose_name='Дата истечения срока давности документа', blank=False)
    IsActive = models.BooleanField(verbose_name='Активный', default=True)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return f'{self.DocumentTypeID}'