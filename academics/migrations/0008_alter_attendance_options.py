# Generated by Django 4.2.7 on 2023-12-13 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0007_remove_attendance_student'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'ordering': ['-created']},
        ),
    ]
