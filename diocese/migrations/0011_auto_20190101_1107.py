# Generated by Django 2.0 on 2019-01-01 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diocese', '0010_auto_20181222_0003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_name', models.CharField(max_length=230)),
                ('order_abbreviation', models.CharField(max_length=30)),
                ('order_priest', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='priest',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='diocese.Order'),
        ),
    ]
