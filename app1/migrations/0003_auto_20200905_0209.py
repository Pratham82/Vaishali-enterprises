# Generated by Django 3.1 on 2020-09-04 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_auto_20200905_0144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='image',
            field=models.ImageField(default='', upload_to='app1/images'),
        ),
    ]
