# Generated by Django 3.1.2 on 2020-10-29 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_auto_20201029_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
