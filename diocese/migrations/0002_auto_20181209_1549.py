# Generated by Django 2.0 on 2018-12-09 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diocese', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archdiocese',
            name='change_date',
            field=models.DateField(verbose_name='date established'),
        ),
        migrations.AlterField(
            model_name='archdiocese',
            name='end_date',
            field=models.DateField(verbose_name='date established'),
        ),
        migrations.AlterField(
            model_name='archdiocese',
            name='establish_date',
            field=models.DateField(verbose_name='date established'),
        ),
        migrations.AlterField(
            model_name='diocese',
            name='change_date',
            field=models.DateField(verbose_name='date established'),
        ),
        migrations.AlterField(
            model_name='diocese',
            name='end_date',
            field=models.DateField(verbose_name='date established'),
        ),
        migrations.AlterField(
            model_name='diocese',
            name='establish_date',
            field=models.DateField(verbose_name='date established'),
        ),
    ]