# Generated by Django 4.2.3 on 2023-08-12 18:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DealerCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('center_name', models.CharField(max_length=100, unique=True, verbose_name='Название центра')),
                ('selling', models.BooleanField(default=False, verbose_name='Продажа ТС')),
                ('repair', models.BooleanField(default=False, verbose_name='Ремонт ТС')),
                ('parts_stor', models.BooleanField(default=False, verbose_name='Склад ЗЧ')),
                ('vehicle_stor', models.BooleanField(default=False, verbose_name='Склад ТС')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Дилер')),
            ],
            options={
                'db_table': 'dealer_centers',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(max_length=5, unique=True, verbose_name='#VIN')),
                ('brand', models.CharField(max_length=50, verbose_name='Бренд')),
                ('m_type', models.CharField(max_length=50, verbose_name='Модель')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет')),
                ('date_arr', models.DateField(verbose_name='Дата поступления к дилеру')),
                ('date_dc', models.DateField(verbose_name='Дата поступления в дилерский центр')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Дилер')),
                ('dealer_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dcenters.dealercenter', verbose_name='Дилерский центр')),
            ],
            options={
                'db_table': 'vehicles',
                'ordering': ['id'],
            },
        ),
    ]
