# Generated by Django 3.1 on 2020-09-05 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_site_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='site',
            old_name='site_name',
            new_name='clientName',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='category',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='site',
            old_name='subcategory',
            new_name='status',
        ),
    ]
