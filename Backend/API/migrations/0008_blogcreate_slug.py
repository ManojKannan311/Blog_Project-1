# Generated by Django 4.2.3 on 2023-10-16 17:47

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_alter_blogcreate_category_alter_blogcreate_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcreate',
            name='Slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='Title', unique=True),
        ),
    ]
