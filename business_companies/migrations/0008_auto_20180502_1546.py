# Generated by Django 2.0.4 on 2018-05-02 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business_companies', '0007_auto_20180501_1605'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='officer',
            options={'managed': True, 'ordering': ['dropped', 'coid__name', 'last'], 'verbose_name_plural': 'Officers'},
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='birthday',
            field=models.DateField(blank=True, db_column='Birthday', null=True, verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='degree',
            field=models.CharField(blank=True, db_column='Degree', help_text='Degree suffix such as "M.D.".', max_length=50, null=True, verbose_name='Degree suffix'),
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='director',
            field=models.IntegerField(blank=True, db_column='Director', help_text='True (1) or False (0) whether this person is a director.', null=True, verbose_name='Is director'),
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='dropped',
            field=models.IntegerField(blank=True, db_column='Dropped', help_text='True (1) or False (0) on whether this person is no longer with company and should not show up in publication.', null=True, verbose_name='Is dropped'),
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='email',
            field=models.CharField(blank=True, db_column='Email', max_length=200, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='first',
            field=models.CharField(blank=True, db_column='First', max_length=200, null=True, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='footnotes',
            field=models.TextField(blank=True, db_column='Footnotes', help_text='Any footnotes to be used in publication.', null=True, verbose_name='Footnotes'),
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='gender',
            field=models.CharField(blank=True, db_column='Gender', help_text='Gender as either M, F, or blank', max_length=50, null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='id',
            field=models.IntegerField(blank=True, db_column='ID', db_index=True, help_text='This is an auto incrementing ID that should not need to be manually created or updated.', verbose_name='Officer ID'),
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='last',
            field=models.CharField(db_column='Last', max_length=200, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='lineage',
            field=models.CharField(blank=True, db_column='Lineage', help_text='Name suffix or lineage.', max_length=50, null=True, verbose_name='Lineage suffix'),
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='middle',
            field=models.CharField(blank=True, db_column='Middle', max_length=50, null=True, verbose_name='Middle name'),
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='notes',
            field=models.TextField(blank=True, db_column='Notes', help_text='Any internal notes about this company.', null=True, verbose_name='Internal notes'),
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='phone',
            field=models.CharField(blank=True, db_column='Phone', max_length=30, null=True, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='race',
            field=models.CharField(blank=True, db_column='Race', help_text='This field is not standardized or consistenly used so is probably not a reliable field for publication.', max_length=50, null=True, verbose_name='Race'),
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='salut',
            field=models.CharField(blank=True, db_column='Salut', help_text='Name prefix', max_length=50, null=True, verbose_name='Salut'),
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='tenure',
            field=models.CharField(blank=True, db_column='Tenure', help_text='Year this officer joined the company.', max_length=200, null=True, verbose_name='Tenure'),
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='title',
            field=models.CharField(blank=True, db_column='Title', help_text='The current title of the officer.', max_length=110, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='historicalofficer',
            name='twitter',
            field=models.CharField(blank=True, db_column='Twitter', max_length=200, null=True, verbose_name='Twitter handle'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='birthday',
            field=models.DateField(blank=True, db_column='Birthday', null=True, verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='coid',
            field=models.ForeignKey(db_column='COID', help_text='Company associated with this record.', on_delete=django.db.models.deletion.CASCADE, to='business_companies.Company', verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='degree',
            field=models.CharField(blank=True, db_column='Degree', help_text='Degree suffix such as "M.D.".', max_length=50, null=True, verbose_name='Degree suffix'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='director',
            field=models.IntegerField(blank=True, db_column='Director', help_text='True (1) or False (0) whether this person is a director.', null=True, verbose_name='Is director'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='dropped',
            field=models.IntegerField(blank=True, db_column='Dropped', help_text='True (1) or False (0) on whether this person is no longer with company and should not show up in publication.', null=True, verbose_name='Is dropped'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='email',
            field=models.CharField(blank=True, db_column='Email', max_length=200, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='first',
            field=models.CharField(blank=True, db_column='First', max_length=200, null=True, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='footnotes',
            field=models.TextField(blank=True, db_column='Footnotes', help_text='Any footnotes to be used in publication.', null=True, verbose_name='Footnotes'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='gender',
            field=models.CharField(blank=True, db_column='Gender', help_text='Gender as either M, F, or blank', max_length=50, null=True, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='id',
            field=models.AutoField(db_column='ID', help_text='This is an auto incrementing ID that should not need to be manually created or updated.', primary_key=True, serialize=False, verbose_name='Officer ID'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='last',
            field=models.CharField(db_column='Last', max_length=200, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='lineage',
            field=models.CharField(blank=True, db_column='Lineage', help_text='Name suffix or lineage.', max_length=50, null=True, verbose_name='Lineage suffix'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='middle',
            field=models.CharField(blank=True, db_column='Middle', max_length=50, null=True, verbose_name='Middle name'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='notes',
            field=models.TextField(blank=True, db_column='Notes', help_text='Any internal notes about this company.', null=True, verbose_name='Internal notes'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='phone',
            field=models.CharField(blank=True, db_column='Phone', max_length=30, null=True, verbose_name='Phone number'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='race',
            field=models.CharField(blank=True, db_column='Race', help_text='This field is not standardized or consistenly used so is probably not a reliable field for publication.', max_length=50, null=True, verbose_name='Race'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='salut',
            field=models.CharField(blank=True, db_column='Salut', help_text='Name prefix', max_length=50, null=True, verbose_name='Salut'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='tenure',
            field=models.CharField(blank=True, db_column='Tenure', help_text='Year this officer joined the company.', max_length=200, null=True, verbose_name='Tenure'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='title',
            field=models.CharField(blank=True, db_column='Title', help_text='The current title of the officer.', max_length=110, null=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='officer',
            name='twitter',
            field=models.CharField(blank=True, db_column='Twitter', max_length=200, null=True, verbose_name='Twitter handle'),
        ),
    ]
