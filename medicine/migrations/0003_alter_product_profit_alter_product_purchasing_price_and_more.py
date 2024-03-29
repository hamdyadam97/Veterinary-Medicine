# Generated by Django 4.2.2 on 2023-08-28 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0002_alter_product_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='profit',
            field=models.DecimalField(decimal_places=2, default=0, error_messages={'name': {'max_length': 'The price must be between 0 and 9999.99.'}}, help_text='Maximum 99999.99', max_digits=7, verbose_name='profit price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='purchasing_price',
            field=models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': 'The price must be between 0 and 9999.99.'}}, help_text='Maximum 99999.99', max_digits=7, verbose_name='purchasing price'),
        ),
        migrations.AlterField(
            model_name='product',
            name='tax_rate',
            field=models.DecimalField(decimal_places=2, default=0, error_messages={'name': {'max_length': 'The price must be between 0 and 9999.99.'}}, help_text='Maximum 99999.99', max_digits=7, verbose_name='tax rate price'),
        ),
    ]
