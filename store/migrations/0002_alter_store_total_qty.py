# Generated by Django 4.2.2 on 2023-08-28 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='total_qty',
            field=models.CharField(default=0, max_length=20),
        ),
    ]