# Generated by Django 3.2.12 on 2022-08-08 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0039_remove_application_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='Axis_Capital_Amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='Axis_Interest',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='Axis_Message',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='Axis_Status',
            field=models.TextField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='HDFC_Capital_Amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='HDFC_Interest',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='HDFC_Message',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='HDFC_Status',
            field=models.TextField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='PNB_Capital_Amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='PNB_Interest',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='PNB_Message',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='PNB_Status',
            field=models.TextField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', max_length=100),
        ),
        migrations.AlterField(
            model_name='application',
            name='SBI_Capital_Amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='SBI_Interest',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='SBI_Message',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='SBI_Status',
            field=models.TextField(choices=[('Approved', 'Approved'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='Pending', max_length=100),
        ),
    ]
