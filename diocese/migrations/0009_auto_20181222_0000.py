# Generated by Django 2.0 on 2018-12-22 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diocese', '0008_archdiocesechurch_church_churchassignment_deacon_dioceseassignment_priest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priest',
            name='year_ordained',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
