from django.db import models

class Sex(models.Model):
    SexTitleFull = models.CharField(verbose_name='Полное название пола', max_length=50, blank=False)
    SexTitleShort = models.CharField(verbose_name='Короткое название пола', max_length=10, blank=False)
    IsActive = models.BooleanField(verbose_name='Активный', default=True)

    class Meta:
        verbose_name = 'Пол'

    def __str__(self):
        return f'{self.SexTitleFull}'

class TreatmentType(models.Model):
    TreatmentTypeTitle = models.CharField(verbose_name='Статус человека', max_length=20, blank=False)
    IsActive = models.BooleanField(verbose_name='Активный', default=True)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return f'{self.TreatmentTypeTitle}'

class Person(models.Model):
    PersonFirstName = models.CharField(verbose_name='Имя', max_length=100, blank=False)
    PersonSecondName = models.CharField(verbose_name='Фамилия', max_length=100, blank=False)
    PersonLastName = models.CharField(verbose_name='Отчество', max_length=100, blank=False)
    PersonDataBirth = models.DateField(verbose_name='Дата рождения', blank=False)
    TreatmentTypeID = models.ForeignKey(TreatmentType, verbose_name='Статус', on_delete=models.CASCADE, blank=False)
    SexID = models.ForeignKey(Sex, verbose_name='Пол', on_delete=models.CASCADE, blank=False)
    IsActive = models.BooleanField(verbose_name='Активный', default=True)

    class Meta:
        verbose_name = 'Человк'
        verbose_name_plural = 'Люди'

    def __str__(self):
        return f'{self.PersonSecondName}'
