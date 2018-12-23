# Generated by Django 2.0 on 2018-12-10 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diocese', '0006_diocese_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diocese',
            name='parent',
        ),
        migrations.AddField(
            model_name='diocese',
            name='created_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='diocese.Diocese'),
        ),
    ]