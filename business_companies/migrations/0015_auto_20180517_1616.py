# Generated by Django 2.0.5 on 2018-05-17 21:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business_companies', '0014_auto_20180515_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='seealsoid',
            field=models.ForeignKey(
                blank=True,
                db_column='SeeAlsoID',
                help_text='The company ID to any related reference.',
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='see_also_company',
                to='business_companies.Company',
                verbose_name='See also company'),
        ),
        migrations.AlterField(
            model_name='employees',
            name='coid',
            field=models.ForeignKey(
                db_column='COID',
                help_text='The associated company with this data.',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='employees_company',
                to='business_companies.Company',
                verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='finances',
            name='coid',
            field=models.ForeignKey(
                db_column='COID',
                help_text='Company associated with this record.',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='finances_company',
                to='business_companies.Company',
                verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='coid',
            field=models.ForeignKey(
                db_column='COID',
                help_text='Company associated with this record.',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='officer_company',
                to='business_companies.Company',
                verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='officerid',
            field=models.ForeignKey(
                db_column='OfficerID',
                help_text='The related officer record.',
                on_delete=django.db.models.deletion.CASCADE,
                related_name='salary_officer',
                to='business_companies.Officer',
                verbose_name='Officer'),
        ),
    ]
