# Generated by Django 4.2.3 on 2023-10-16 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_blogcreate_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcreate',
            name='Key_Word',
            field=models.CharField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='blogcreate',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]