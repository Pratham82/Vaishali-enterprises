# Generated by Django 3.1 on 2020-09-04 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20200905_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='image',
            field=models.ImageField(default='', upload_to='media_files/images'),
        ),
    ]