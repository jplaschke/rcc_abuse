# Generated by Django 2.0 on 2018-12-10 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diocese', '0005_auto_20181209_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='diocese',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diocese.Diocese'),
        ),
    ]
