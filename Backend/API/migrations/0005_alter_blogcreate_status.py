# Generated by Django 4.2.3 on 2023-10-09 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_alter_blogcreate_status_alter_blogcreate_trending'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcreate',
            name='Status',
            field=models.BooleanField(default=False, help_text='0-Show ,1-Hide'),
        ),
    ]
