# Generated by Django 3.2.12 on 2022-08-12 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0043_auto_20220809_1024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='Axis_Message',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='application',
            name='HDFC_Message',
        ),
        migrations.RemoveField(
            model_name='application',
            name='PNB_Message',
        ),
        migrations.RemoveField(
            model_name='application',
            name='SBI_Message',
        ),
        migrations.AddField(
            model_name='application',
            name='bank',
            field=models.TextField(blank=True, choices=[('SBI', 'SBI'), ('PNB', 'PNB'), ('Axis', 'Axis'), ('HDFC', 'HDFC')], default='Choose Bank', max_length=100, null=True),
        ),
    ]
