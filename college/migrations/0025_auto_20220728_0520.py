# Generated by Django 3.2.12 on 2022-07-28 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0024_auto_20210727_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='application',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]