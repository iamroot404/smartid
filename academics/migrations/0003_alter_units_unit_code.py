# Generated by Django 4.2.7 on 2023-11-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0002_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='units',
            name='unit_code',
            field=models.CharField(max_length=200),
        ),
    ]
