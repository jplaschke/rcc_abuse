# Generated by Django 2.0 on 2019-01-09 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diocese', '0013_remove_priest_order_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='priest',
            name='clergy_type',
            field=models.CharField(choices=[('P', 'Priest'), ('N', 'Nun'), ('B', 'Brother'), ('S', 'Seminarian'), ('D', 'Deacon')], default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='priest',
            name='notes',
            field=models.CharField(max_length=5000),
        ),
    ]
