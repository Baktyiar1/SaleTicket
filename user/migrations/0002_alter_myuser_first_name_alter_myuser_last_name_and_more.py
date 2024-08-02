# Generated by Django 5.0.7 on 2024-07-24 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Обычный пользователь'), (2, 'Менеджер'), (3, 'Бухгалтер')]),
        ),
    ]
