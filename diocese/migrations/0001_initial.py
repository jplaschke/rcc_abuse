# Generated by Django 2.0 on 2018-12-09 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Archdiocese',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('mother_church_name', models.CharField(max_length=200)),
                ('mother_church_address', models.CharField(max_length=200)),
                ('mother_church_zipcode', models.CharField(max_length=200)),
                ('establish_date', models.DateTimeField(verbose_name='date established')),
                ('change_date', models.DateTimeField(verbose_name='date established')),
                ('end_date', models.DateTimeField(verbose_name='date established')),
            ],
        ),
        migrations.CreateModel(
            name='Diocese',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('establish_date', models.DateTimeField(verbose_name='date established')),
                ('change_date', models.DateTimeField(verbose_name='date established')),
                ('end_date', models.DateTimeField(verbose_name='date established')),
                ('archdiocese', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diocese.Archdiocese')),
            ],
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveSmallIntegerField()),
                ('total_priests', models.PositiveSmallIntegerField()),
                ('num_parishes', models.PositiveSmallIntegerField()),
                ('diocese', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diocese.Diocese')),
            ],
        ),
    ]
