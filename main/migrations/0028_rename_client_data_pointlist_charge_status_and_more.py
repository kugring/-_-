# Generated by Django 5.0.1 on 2024-02-26 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_orderlist_modified_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pointlist',
            old_name='client_data',
            new_name='charge_status',
        ),
        migrations.AddField(
            model_name='pointlist',
            name='client_name',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='pointlist',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pointlist',
            name='manager',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
