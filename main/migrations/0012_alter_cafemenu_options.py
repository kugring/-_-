# Generated by Django 5.0.1 on 2024-01-12 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_cafeoption_option_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafemenu',
            name='options',
            field=models.CharField(default='', max_length=255),
        ),
    ]
