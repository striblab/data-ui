# Generated by Django 2.0.4 on 2018-05-03 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business_companies', '0008_auto_20180502_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='added',
            field=models.DateField(db_column='Added', help_text='Date added.', verbose_name='Added'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='allothertotal',
            field=models.FloatField(blank=True, db_column='AllOtherTotal', help_text='(Unsure?)', null=True, verbose_name='All other total'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='bonus',
            field=models.FloatField(blank=True, db_column='Bonus', null=True, verbose_name='Bonus'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='bonuschange',
            field=models.FloatField(blank=True, db_column='BonusChange', help_text='(Deprecated, managed in previous records)', null=True),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='bonussalary',
            field=models.FloatField(blank=True, db_column='BonusSalary', help_text='(Deprecated, calculated)', null=True, verbose_name='Subtotal: Bonus and salary'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='ceo',
            field=models.IntegerField(blank=True, db_column='CEO', help_text='(Deprecated, see Officer record) True (1) or False (0) on whether this is a CEO or not.', null=True, verbose_name='Is CEO'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='ceopayratio',
            field=models.FloatField(blank=True, db_column='CEOPayRatio', help_text='Ratio of CEO to (average?) employee pay.', null=True, verbose_name='CEO pay ratio'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='extratotal',
            field=models.FloatField(blank=True, db_column='ExtraTotal', help_text='(Unsure?)', null=True, verbose_name='Extra total'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='fiscalyearend',
            field=models.DateField(db_column='FiscalYearEnd', help_text='Date of the fiscal year end.', verbose_name='Fiscal year end'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='flag',
            field=models.IntegerField(blank=True, db_column='Flag', help_text='(Unsure?)', null=True, verbose_name='Flag'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='footnotes',
            field=models.TextField(blank=True, db_column='Footnotes', help_text='Any footnotes to be used in publication.', null=True, verbose_name='Footnotes'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='fullyear',
            field=models.IntegerField(blank=True, db_column='FullYear', help_text='True (1) or False (0) whether this data is for the full fiscal year.', null=True, verbose_name='Is full year'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='id',
            field=models.IntegerField(blank=True, db_column='ID', db_index=True, help_text='This is an auto incrementing ID that should not need to be manually created or updated.', verbose_name='Officer Salary ID'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='longtermchange',
            field=models.FloatField(blank=True, db_column='LongTermChange', help_text='(Deprecated, calculated)', null=True),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='longtermtotal',
            field=models.FloatField(blank=True, db_column='LongTermTotal', help_text='(Unsure?)', null=True, verbose_name='Long term total'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='medianemployeepay',
            field=models.FloatField(blank=True, db_column='MedianEmployeePay', null=True, verbose_name='Median employee pay'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='nonequityipc',
            field=models.FloatField(blank=True, db_column='NonEquityIPC', help_text='(Unsure?)', null=True, verbose_name='Non-equity IPC'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='notes',
            field=models.TextField(blank=True, db_column='Notes', help_text='Any internal notes about this company.', null=True, verbose_name='Internal notes'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='nr',
            field=models.IntegerField(blank=True, db_column='NR', help_text='(Unsure?)', null=True, verbose_name='NR'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='optionaward',
            field=models.FloatField(blank=True, db_column='OptionAward', help_text='(Unsure?)', null=True, verbose_name='Option awards'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='optionsexercisablevalue',
            field=models.FloatField(blank=True, db_column='OptionsExercisableValue', null=True, verbose_name='Options exercisable value'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='optionsunexercisablevalue',
            field=models.FloatField(blank=True, db_column='OptionsUnexercisableValue', null=True, verbose_name='Options unexercisable value'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='othertotal',
            field=models.FloatField(blank=True, db_column='OtherTotal', help_text='(Unsure?)', null=True, verbose_name='Other total'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='pensionchange',
            field=models.FloatField(blank=True, db_column='PensionChange', help_text='(Deprecated, calculated)', null=True),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='performance',
            field=models.FloatField(blank=True, db_column='Performance', help_text='(Unsure?)', null=True, verbose_name='Performance'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='publishyear',
            field=models.IntegerField(db_column='PublishYear', help_text='Year this record is used for publishing.', verbose_name='Publish year'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='restricted',
            field=models.FloatField(blank=True, db_column='Restricted', help_text='(Unsure?)', null=True, verbose_name='Restricted'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='salary',
            field=models.FloatField(blank=True, db_column='Salary', help_text='Base salary for officer.', null=True, verbose_name='Base salary'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='salarychange',
            field=models.FloatField(blank=True, db_column='SalaryChange', help_text='(Deprecated, managed in previous records)', null=True),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='salarystatus',
            field=models.CharField(blank=True, db_column='SalaryStatus', help_text='(Unsure what is used for)', max_length=50, null=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='sayonpay',
            field=models.FloatField(blank=True, db_column='SayOnPay', help_text='(Unsure?)', null=True, verbose_name='Say on pay'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='sharesvesting',
            field=models.FloatField(blank=True, db_column='SharesVesting', help_text='(Unsure?)', null=True, verbose_name='Shares vesting'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='stockaward',
            field=models.FloatField(blank=True, db_column='StockAward', help_text='(Unsure?)', null=True, verbose_name='Stock awards'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='stockchange',
            field=models.FloatField(blank=True, db_column='StockChange', help_text='(Deprecated, calculated)', null=True),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='stockexpense',
            field=models.FloatField(blank=True, db_column='StockExpense', help_text='(Unsure?)', null=True, verbose_name='Stock expenses'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='stockoptions',
            field=models.FloatField(blank=True, db_column='StockOptions', help_text='Number of stock options.', null=True, verbose_name='Stock options'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='stockoptionsvalue',
            field=models.FloatField(blank=True, db_column='StockOptionsValue', help_text='Value of stock options.', null=True, verbose_name='Value of stock options'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='title',
            field=models.CharField(blank=True, db_column='Title', help_text='(Deprecated, see Officer record)', max_length=100, null=True, verbose_name='Officer title'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='total',
            field=models.FloatField(blank=True, db_column='Total', help_text='(Unsure?  Should be calculated?)', null=True, verbose_name='Total pay'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='totalchange',
            field=models.FloatField(blank=True, db_column='TotalChange', help_text='(Deprecated, calculated)', null=True),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='totalltequitysct',
            field=models.FloatField(blank=True, db_column='TotalLTEquitySCT', help_text='(Unsure?)', null=True, verbose_name='Total LT equity SCT'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='totalsb',
            field=models.FloatField(blank=True, db_column='TotalSB', help_text='(Unsure?)', null=True, verbose_name='Total SB'),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='totalsbchange',
            field=models.FloatField(blank=True, db_column='TotalSBChange', help_text='(Deprecated, calculated)', null=True),
        ),
        migrations.AlterField(
            model_name='historicalofficersalary',
            name='ylabel',
            field=models.IntegerField(blank=True, db_column='YLabel', help_text='(Unsure?)', null=True, verbose_name='Y Label'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='added',
            field=models.DateField(db_column='Added', help_text='Date added.', verbose_name='Added'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='allothertotal',
            field=models.FloatField(blank=True, db_column='AllOtherTotal', help_text='(Unsure?)', null=True, verbose_name='All other total'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='bonus',
            field=models.FloatField(blank=True, db_column='Bonus', null=True, verbose_name='Bonus'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='bonuschange',
            field=models.FloatField(blank=True, db_column='BonusChange', help_text='(Deprecated, managed in previous records)', null=True),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='bonussalary',
            field=models.FloatField(blank=True, db_column='BonusSalary', help_text='(Deprecated, calculated)', null=True, verbose_name='Subtotal: Bonus and salary'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='ceo',
            field=models.IntegerField(blank=True, db_column='CEO', help_text='(Deprecated, see Officer record) True (1) or False (0) on whether this is a CEO or not.', null=True, verbose_name='Is CEO'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='ceopayratio',
            field=models.FloatField(blank=True, db_column='CEOPayRatio', help_text='Ratio of CEO to (average?) employee pay.', null=True, verbose_name='CEO pay ratio'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='extratotal',
            field=models.FloatField(blank=True, db_column='ExtraTotal', help_text='(Unsure?)', null=True, verbose_name='Extra total'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='fiscalyearend',
            field=models.DateField(db_column='FiscalYearEnd', help_text='Date of the fiscal year end.', verbose_name='Fiscal year end'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='flag',
            field=models.IntegerField(blank=True, db_column='Flag', help_text='(Unsure?)', null=True, verbose_name='Flag'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='footnotes',
            field=models.TextField(blank=True, db_column='Footnotes', help_text='Any footnotes to be used in publication.', null=True, verbose_name='Footnotes'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='fullyear',
            field=models.IntegerField(blank=True, db_column='FullYear', help_text='True (1) or False (0) whether this data is for the full fiscal year.', null=True, verbose_name='Is full year'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='id',
            field=models.AutoField(db_column='ID', help_text='This is an auto incrementing ID that should not need to be manually created or updated.', primary_key=True, serialize=False, verbose_name='Officer Salary ID'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='longtermchange',
            field=models.FloatField(blank=True, db_column='LongTermChange', help_text='(Deprecated, calculated)', null=True),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='longtermtotal',
            field=models.FloatField(blank=True, db_column='LongTermTotal', help_text='(Unsure?)', null=True, verbose_name='Long term total'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='medianemployeepay',
            field=models.FloatField(blank=True, db_column='MedianEmployeePay', null=True, verbose_name='Median employee pay'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='nonequityipc',
            field=models.FloatField(blank=True, db_column='NonEquityIPC', help_text='(Unsure?)', null=True, verbose_name='Non-equity IPC'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='notes',
            field=models.TextField(blank=True, db_column='Notes', help_text='Any internal notes about this company.', null=True, verbose_name='Internal notes'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='nr',
            field=models.IntegerField(blank=True, db_column='NR', help_text='(Unsure?)', null=True, verbose_name='NR'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='officerid',
            field=models.ForeignKey(db_column='OfficerID', help_text='The related officer record.', on_delete=django.db.models.deletion.DO_NOTHING, to='business_companies.Officer', verbose_name='Officer'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='optionaward',
            field=models.FloatField(blank=True, db_column='OptionAward', help_text='(Unsure?)', null=True, verbose_name='Option awards'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='optionsexercisablevalue',
            field=models.FloatField(blank=True, db_column='OptionsExercisableValue', null=True, verbose_name='Options exercisable value'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='optionsunexercisablevalue',
            field=models.FloatField(blank=True, db_column='OptionsUnexercisableValue', null=True, verbose_name='Options unexercisable value'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='othertotal',
            field=models.FloatField(blank=True, db_column='OtherTotal', help_text='(Unsure?)', null=True, verbose_name='Other total'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='pensionchange',
            field=models.FloatField(blank=True, db_column='PensionChange', help_text='(Deprecated, calculated)', null=True),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='performance',
            field=models.FloatField(blank=True, db_column='Performance', help_text='(Unsure?)', null=True, verbose_name='Performance'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='publishyear',
            field=models.IntegerField(db_column='PublishYear', help_text='Year this record is used for publishing.', verbose_name='Publish year'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='restricted',
            field=models.FloatField(blank=True, db_column='Restricted', help_text='(Unsure?)', null=True, verbose_name='Restricted'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='salary',
            field=models.FloatField(blank=True, db_column='Salary', help_text='Base salary for officer.', null=True, verbose_name='Base salary'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='salarychange',
            field=models.FloatField(blank=True, db_column='SalaryChange', help_text='(Deprecated, managed in previous records)', null=True),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='salarystatus',
            field=models.CharField(blank=True, db_column='SalaryStatus', help_text='(Unsure what is used for)', max_length=50, null=True, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='sayonpay',
            field=models.FloatField(blank=True, db_column='SayOnPay', help_text='(Unsure?)', null=True, verbose_name='Say on pay'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='sharesvesting',
            field=models.FloatField(blank=True, db_column='SharesVesting', help_text='(Unsure?)', null=True, verbose_name='Shares vesting'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='stockaward',
            field=models.FloatField(blank=True, db_column='StockAward', help_text='(Unsure?)', null=True, verbose_name='Stock awards'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='stockchange',
            field=models.FloatField(blank=True, db_column='StockChange', help_text='(Deprecated, calculated)', null=True),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='stockexpense',
            field=models.FloatField(blank=True, db_column='StockExpense', help_text='(Unsure?)', null=True, verbose_name='Stock expenses'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='stockoptions',
            field=models.FloatField(blank=True, db_column='StockOptions', help_text='Number of stock options.', null=True, verbose_name='Stock options'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='stockoptionsvalue',
            field=models.FloatField(blank=True, db_column='StockOptionsValue', help_text='Value of stock options.', null=True, verbose_name='Value of stock options'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='title',
            field=models.CharField(blank=True, db_column='Title', help_text='(Deprecated, see Officer record)', max_length=100, null=True, verbose_name='Officer title'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='total',
            field=models.FloatField(blank=True, db_column='Total', help_text='(Unsure?  Should be calculated?)', null=True, verbose_name='Total pay'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='totalchange',
            field=models.FloatField(blank=True, db_column='TotalChange', help_text='(Deprecated, calculated)', null=True),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='totalltequitysct',
            field=models.FloatField(blank=True, db_column='TotalLTEquitySCT', help_text='(Unsure?)', null=True, verbose_name='Total LT equity SCT'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='totalsb',
            field=models.FloatField(blank=True, db_column='TotalSB', help_text='(Unsure?)', null=True, verbose_name='Total SB'),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='totalsbchange',
            field=models.FloatField(blank=True, db_column='TotalSBChange', help_text='(Deprecated, calculated)', null=True),
        ),
        migrations.AlterField(
            model_name='officersalary',
            name='ylabel',
            field=models.IntegerField(blank=True, db_column='YLabel', help_text='(Unsure?)', null=True, verbose_name='Y Label'),
        ),
    ]
