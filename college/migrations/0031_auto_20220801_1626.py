# Generated by Django 3.2.12 on 2022-08-01 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0030_alter_application_capital_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='Application_Status',
            field=models.TextField(blank=True, choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='Bank',
            field=models.TextField(blank=True, choices=[('SBI', 'SBI'), ('PNB', 'PNB'), ('Axis', 'Axis')], default=' ', max_length=100),
        ),
    ]