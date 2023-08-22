from django.db import models
import datetime



class DealerCenter(models.Model):
    dealer = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Дилер')
    center_name = models.CharField(max_length=100, unique=True, verbose_name='Название центра')
    selling = models.BooleanField(default=False, verbose_name='Продажа ТС')
    repair = models.BooleanField(default=False, verbose_name='Ремонт ТС')
    parts_stor = models.BooleanField(default=False, verbose_name='Склад ЗЧ')
    vehicle_stor = models.BooleanField(default=False, verbose_name='Склад ТС')

    def __str__(self):
        return f'{self.dealer} - {self.center_name}'

    class Meta:
        db_table = 'dealer_centers'


class Vehicle(models.Model):
    vin = models.CharField(max_length=5, unique=True, verbose_name='#VIN')
    brand = models.CharField(max_length=50, verbose_name='Бренд')
    m_type = models.CharField(max_length=50, verbose_name='Модель')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    date_arr = models.DateField(verbose_name='Дата поступления к дилеру (ГГГГ-ММ-ДД)')
    date_dc = models.DateField(verbose_name='Дата поступления в дилерский центр (ГГГГ-ММ-ДД)')
    dealer_center = models.ForeignKey(DealerCenter, on_delete=models.CASCADE, verbose_name='Дилерский центр')
    dealer = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Дилер')

    def __str__(self):
        return f'{self.vin} - {self.brand} {self.m_type}'

    class Meta:
        db_table = 'vehicles'
        ordering = ['id']