# Generated by Django 4.1.1 on 2022-10-02 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='vendor_license',
            field=models.ImageField(blank=True, null=True, upload_to='vendor/license'),
        ),
    ]
