from django.db import models

class OverFunds(models.Model):
    '''Модель с общей суммой семейного бюджета'''
    current_date = models.DateField('Дата')
    current_sum = models.IntegerField('Общая сумма')

    class Meta:
        verbose_name = 'Общая сумма средств'

    def __str__(self):
        return self.current_sum


class Users(models.Model):
    '''Модель Члены семьи'''
    name = models.CharField('Член семьи', max_length=200)

    class Meta:
        verbose_name = 'Член семьи'

    def __str__(self):
        return self.name


class SourceMoney(models.Model):
    '''Модель "Источники средств наличка/карта visa и т.д.'''
    type = models.CharField('Тип средств', max_length=50)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    sum = models.IntegerField('Сумма')

    class Meta:
        verbose_name = 'Тип средств'

    def __str__(self):
        return self.type


class TransType(models.Model):
    '''Модель типа транзакции (приход/расход)'''
    type = models.CharField('Тип транзакции', max_length=50)

    class Meta:
        verbose_name = 'Тип транзакции'

    def __str__(self):
        return self.type

class Trans(models.Model):
    '''Модель транзакции'''
    trans_type = models.ForeignKey(TransType, on_delete=models.CASCADE)
    trans_source = models.ForeignKey(SourceMoney, on_delete=models.CASCADE)
    trans_date = models.DateField()
    trans_sum = models.IntegerField('Сумма')
    comment = models.CharField('Комментарий', max_length=500)

    class Meta:
        verbose_name = 'Транзакция'

    def __str__(self):
        return self.comment

