# Generated by Django 3.1.5 on 2021-01-24 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OverFunds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_date', models.DateField(verbose_name='Дата')),
                ('current_sum', models.IntegerField(verbose_name='Общая сумма')),
            ],
            options={
                'verbose_name': 'Общая сумма средств',
            },
        ),
        migrations.CreateModel(
            name='SourceMoney',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Тип средств')),
                ('sum', models.IntegerField(verbose_name='Сумма')),
            ],
            options={
                'verbose_name': 'Тип средств',
            },
        ),
        migrations.CreateModel(
            name='TransType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50, verbose_name='Тип транзакции')),
            ],
            options={
                'verbose_name': 'Тип транзакции',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Член семьи')),
            ],
            options={
                'verbose_name': 'Член семьи',
            },
        ),
        migrations.CreateModel(
            name='Trans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_date', models.DateField()),
                ('trans_sum', models.IntegerField(verbose_name='Сумма')),
                ('comment', models.CharField(max_length=500, verbose_name='Комментарий')),
                ('trans_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buh.sourcemoney')),
                ('trans_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buh.transtype')),
            ],
            options={
                'verbose_name': 'Транзакция',
            },
        ),
        migrations.AddField(
            model_name='sourcemoney',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buh.users'),
        ),
    ]