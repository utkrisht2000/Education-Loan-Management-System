# Generated by Django 3.2.12 on 2022-08-01 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0028_auto_20220729_0416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='cet_scorecard',
            new_name='Highschool_Marksheet',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='hsc_leaving_certificate',
            new_name='Highschool_Passing_Certificate',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='hsc_percentage',
            new_name='Highschool_Percentage',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='cet_percentile',
            new_name='Interest',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='hsc_marksheet',
            new_name='bank_Passbook',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='jee_percentile',
            new_name='gRE_Score',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='hsc_passing_certificate',
            new_name='gRE_Scorecard',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='jee_scorecard',
            new_name='iELTS_Scorecard',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='ssc_leaving_certificate',
            new_name='identity_Proof',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='ssc_marksheet',
            new_name='intermediate_Marksheet',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='ssc_passing_certificate',
            new_name='intermediate_Passing_Certificate',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='ssc_percentage',
            new_name='intermediate_Percentage',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='course',
            new_name='ms_Course',
        ),
        migrations.RenameField(
            model_name='application',
            old_name='student_profile',
            new_name='profile_Picture',
        ),
        migrations.AddField(
            model_name='application',
            name='Capital_Amount',
            field=models.DecimalField(decimal_places=8, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='iELTS_Score',
            field=models.DecimalField(decimal_places=3, max_digits=5, null=True),
        ),
    ]