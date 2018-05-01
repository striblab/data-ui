# Generated by Django 2.0.4 on 2018-04-26 20:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunSQL(
            "DELETE FROM Companies WHERE COID IS NULL OR COID = ''"
        ),
        migrations.RunSQL(
            # Can't do this with dates, as 0000-00-00 is not valid
            "DELETE FROM Employees WHERE ID = 5711"
        ),
        migrations.RunSQL(
            "ALTER TABLE Companies CHANGE `History` `CompanyHistory` TEXT"
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('coid', models.CharField(db_column='COID', max_length=100, primary_key=True, serialize=False)),
                ('added', models.DateField(db_column='Added')),
                ('irsno', models.CharField(blank=True, db_column='IRSNo', max_length=100, null=True)),
                ('name', models.CharField(blank=True, db_column='Company', max_length=200, null=True)),
                ('companytype', models.CharField(blank=True, db_column='CompanyType', max_length=40, null=True)),
                ('category', models.CharField(blank=True, db_column='Category', max_length=200, null=True)),
                ('alpha', models.CharField(blank=True, db_column='Alpha', max_length=200, null=True)),
                ('seealso', models.CharField(blank=True, db_column='SeeAlso', max_length=100, null=True)),
                ('address1', models.CharField(blank=True, db_column='Address1', max_length=200, null=True)),
                ('address2', models.CharField(blank=True, db_column='Address2', max_length=200, null=True)),
                ('city', models.CharField(blank=True, db_column='City', max_length=100, null=True)),
                ('state', models.CharField(blank=True, db_column='State', max_length=2, null=True)),
                ('zip', models.CharField(blank=True, db_column='Zip', max_length=20, null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=30, null=True)),
                ('fax', models.CharField(blank=True, db_column='Fax', max_length=30, null=True)),
                ('www', models.CharField(blank=True, db_column='WWW', max_length=200, null=True)),
                ('contact', models.CharField(blank=True, db_column='Contact', max_length=200, null=True)),
                ('contactphone', models.CharField(blank=True, db_column='ContactPhone', max_length=30, null=True)),
                ('contactemail', models.CharField(blank=True, db_column='ContactEmail', max_length=200, null=True)),
                ('description', models.TextField(blank=True, db_column='Description', null=True)),
                ('shortdesc', models.CharField(blank=True, db_column='ShortDesc', max_length=750, null=True)),
                ('companyhistory', models.TextField(blank=True, db_column='CompanyHistory', null=True)),
                ('founded', models.IntegerField(blank=True, db_column='Founded', null=True)),
                ('inc', models.IntegerField(blank=True, db_column='Inc', null=True)),
                ('incst', models.CharField(blank=True, db_column='IncSt', max_length=2, null=True)),
                ('stocksymbol', models.CharField(blank=True, db_column='StockSymbol', max_length=12, null=True)),
                ('exchange', models.CharField(blank=True, db_column='Exchange', max_length=50, null=True)),
                ('annualmeet', models.CharField(blank=True, db_column='AnnualMeet', max_length=30, null=True)),
                ('fymonth', models.IntegerField(blank=True, db_column='FYMonth', null=True)),
                ('enteredby', models.CharField(blank=True, db_column='EnteredBy', max_length=30, null=True)),
                ('class_field', models.CharField(blank=True, db_column='Class', max_length=10, null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
                ('footnotes', models.TextField(blank=True, db_column='Footnotes', null=True)),
                ('seealsoid', models.ForeignKey(blank=True, db_column='SeeAlsoID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='business_companies.Company')),
            ],
            options={
                'verbose_name_plural': 'Companies',
                'db_table': 'Companies',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('added', models.DateField(db_column='Added')),
                ('publishyear', models.IntegerField(db_column='PublishYear')),
                ('parttime', models.IntegerField(blank=True, db_column='PartTime', null=True)),
                ('fulltime', models.IntegerField(blank=True, db_column='FullTime', null=True)),
                ('union', models.IntegerField(blank=True, db_column='Union', null=True)),
                ('total', models.IntegerField(blank=True, db_column='Total', null=True)),
                ('minnesota', models.IntegerField(blank=True, db_column='Minnesota', null=True)),
                ('footnotes', models.TextField(blank=True, db_column='Footnotes', null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
                ('coid', models.ForeignKey(db_column='COID', on_delete=django.db.models.deletion.DO_NOTHING, to='business_companies.Company')),
            ],
            options={
                'verbose_name_plural': 'Employees',
                'db_table': 'Employees',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Finances',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('publishyear', models.IntegerField(db_column='PublishYear')),
                ('customrank', models.IntegerField(blank=True, db_column='CustomRank', null=True)),
                ('done', models.CharField(blank=True, db_column='Done', max_length=10, null=True)),
                ('fye', models.DateField(blank=True, db_column='FYE', null=True)),
                ('maxoffye', models.DateField(blank=True, db_column='MaxOfFYE', null=True)),
                ('ceo', models.CharField(blank=True, db_column='CEO', max_length=300, null=True)),
                ('category', models.CharField(blank=True, db_column='Category', max_length=300, null=True)),
                ('revenue', models.FloatField(blank=True, db_column='Revenue', null=True)),
                ('ati', models.FloatField(blank=True, db_column='ATI', null=True)),
                ('netincome', models.FloatField(blank=True, db_column='NetIncome', null=True)),
                ('earningspershare', models.FloatField(blank=True, db_column='EarningsPerShare', null=True)),
                ('totalassets', models.FloatField(blank=True, db_column='TotalAssets', null=True)),
                ('shareholdersequity', models.FloatField(blank=True, db_column='ShareholdersEquity', null=True)),
                ('debt', models.FloatField(blank=True, db_column='Debt', null=True)),
                ('shares', models.FloatField(blank=True, db_column='Shares', null=True)),
                ('totalemployees', models.IntegerField(blank=True, db_column='TotalEmployees', null=True)),
                ('mnemployees', models.IntegerField(blank=True, db_column='MNEmployees', null=True)),
                ('marketcap', models.FloatField(blank=True, db_column='MarketCap', null=True)),
                ('empdate', models.DateField(blank=True, db_column='EMPDate', null=True)),
                ('prevyearfye', models.DateField(blank=True, db_column='PrevYearFYE', null=True)),
                ('prevyearrevenue', models.FloatField(blank=True, db_column='PrevYearRevenue', null=True)),
                ('prevyearati', models.FloatField(blank=True, db_column='PrevYearATI', null=True)),
                ('prevyearnetincome', models.FloatField(blank=True, db_column='PrevYearNetIncome', null=True)),
                ('prevyearearnpershare', models.FloatField(blank=True, db_column='PrevYearEarnPerShare', null=True)),
                ('prevyeartotalassets', models.FloatField(blank=True, db_column='PrevYearTotalAssets', null=True)),
                ('prevyearshareequity', models.FloatField(blank=True, db_column='PrevYearShareEquity', null=True)),
                ('prevyeardebt', models.FloatField(blank=True, db_column='PrevYearDebt', null=True)),
                ('prevyearshares', models.FloatField(blank=True, db_column='PrevYearShares', null=True)),
                ('prevyeartotalemp', models.IntegerField(blank=True, db_column='PrevYearTotalEmp', null=True)),
                ('prevyearmnemp', models.IntegerField(blank=True, db_column='PrevYearMNEmp', null=True)),
                ('prevyearmarketcap', models.FloatField(blank=True, db_column='PrevYearMarketCap', null=True)),
                ('prevyearclose', models.FloatField(blank=True, db_column='PrevYearClose', null=True)),
                ('customrankrevenue', models.IntegerField(blank=True, db_column='CustomRankRevenue', null=True)),
                ('customrankprofit', models.IntegerField(blank=True, db_column='CustomRankProfit', null=True)),
                ('customrankassets', models.IntegerField(blank=True, db_column='CustomRankAssets', null=True)),
                ('customrankmarketcap', models.IntegerField(blank=True, db_column='CustomRankMarketCap', null=True)),
                ('customrankblend', models.IntegerField(blank=True, db_column='CustomRankBlend', null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
                ('footnotes', models.TextField(blank=True, db_column='Footnotes', null=True)),
                ('coid', models.ForeignKey(db_column='COID', on_delete=django.db.models.deletion.DO_NOTHING, to='business_companies.Company')),
            ],
            options={
                'verbose_name_plural': 'Finances',
                'db_table': 'Finances',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NonprofitFinances',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('added', models.DateField(db_column='Added')),
                ('publishyear', models.IntegerField(db_column='PublishYear')),
                ('status', models.CharField(blank=True, db_column='Status', max_length=50, null=True)),
                ('fiscalyearend', models.DateField(db_column='FiscalYearEnd')),
                ('annualreportdate', models.DateField(db_column='AnnualReportDate')),
                ('source', models.CharField(blank=True, db_column='Source', max_length=512, null=True)),
                ('contribgrants', models.FloatField(blank=True, db_column='ContribGrants', null=True)),
                ('revenue', models.FloatField(blank=True, db_column='Revenue', null=True)),
                ('expenses', models.FloatField(blank=True, db_column='Expenses', null=True)),
                ('excess', models.FloatField(blank=True, db_column='Excess', null=True)),
                ('programservicerevenue', models.FloatField(blank=True, db_column='ProgramServiceRevenue', null=True)),
                ('investgainslosses', models.FloatField(blank=True, db_column='InvestGainsLosses', null=True)),
                ('programserviceexpense', models.FloatField(blank=True, db_column='ProgramServiceExpense', null=True)),
                ('managementgeneralexpenses', models.FloatField(blank=True, db_column='ManagementGeneralExpenses', null=True)),
                ('fundraisingexpenses', models.FloatField(blank=True, db_column='FundraisingExpenses', null=True)),
                ('eoybalance', models.FloatField(blank=True, db_column='EOYBalance', null=True)),
                ('inputsource', models.CharField(blank=True, db_column='InputSource', max_length=512, null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
                ('footnotes', models.TextField(blank=True, db_column='Footnotes', null=True)),
                ('coid', models.ForeignKey(db_column='COID', on_delete=django.db.models.deletion.DO_NOTHING, to='business_companies.Company')),
            ],
            options={
                'verbose_name_plural': 'NonProfit Finances',
                'db_table': 'NonProfit_Finances',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NonprofitSalary',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('added', models.DateField(db_column='Added')),
                ('publishyear', models.IntegerField(db_column='PublishYear')),
                ('salarystatus', models.CharField(blank=True, db_column='SalaryStatus', max_length=50, null=True)),
                ('fiscalyearend', models.DateField(db_column='FiscalYearEnd')),
                ('fiscalyearnbr', models.IntegerField(blank=True, db_column='FiscalYearNBR', null=True)),
                ('salary', models.FloatField(blank=True, db_column='Salary', null=True)),
                ('benefit', models.FloatField(blank=True, db_column='Benefit', null=True)),
                ('other', models.FloatField(blank=True, db_column='Other', null=True)),
                ('bonus', models.FloatField(blank=True, db_column='Bonus', null=True)),
                ('deferred', models.FloatField(blank=True, db_column='Deferred', null=True)),
                ('total', models.FloatField(blank=True, db_column='Total', null=True)),
                ('footnotes', models.TextField(blank=True, db_column='Footnotes', null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
                ('officerid', models.ForeignKey(db_column='OfficerID', on_delete=django.db.models.deletion.DO_NOTHING, to='business_companies.Officer')),
            ],
            options={
                'verbose_name_plural': 'NonProfit Salaries',
                'db_table': 'NonProfit_Salaries',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('dropped', models.IntegerField(blank=True, db_column='Dropped', null=True)),
                ('salut', models.CharField(blank=True, db_column='Salut', max_length=50, null=True)),
                ('first', models.CharField(blank=True, db_column='First', max_length=200, null=True)),
                ('middle', models.CharField(blank=True, db_column='Middle', max_length=50, null=True)),
                ('last', models.CharField(db_column='Last', max_length=200)),
                ('lineage', models.CharField(blank=True, db_column='Lineage', max_length=50, null=True)),
                ('degree', models.CharField(blank=True, db_column='Degree', max_length=50, null=True)),
                ('gender', models.CharField(blank=True, db_column='Gender', max_length=50, null=True)),
                ('race', models.CharField(blank=True, db_column='Race', max_length=50, null=True)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=110, null=True)),
                ('director', models.IntegerField(blank=True, db_column='Director', null=True)),
                ('birthday', models.DateField(blank=True, db_column='Birthday', null=True)),
                ('tenure', models.CharField(blank=True, db_column='Tenure', max_length=200, null=True)),
                ('phone', models.CharField(blank=True, db_column='Phone', max_length=30, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=200, null=True)),
                ('twitter', models.CharField(blank=True, db_column='Twitter', max_length=200, null=True)),
                ('footnotes', models.TextField(blank=True, db_column='Footnotes', null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
                ('coid', models.ForeignKey(db_column='COID', on_delete=django.db.models.deletion.DO_NOTHING, to='business_companies.Company')),
            ],
            options={
                'verbose_name_plural': 'Officers',
                'db_table': 'Officers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OfficerSalary',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('added', models.DateField(db_column='Added')),
                ('publishyear', models.IntegerField(db_column='PublishYear')),
                ('title', models.CharField(blank=True, db_column='Title', max_length=100, null=True)),
                ('ceo', models.IntegerField(blank=True, db_column='CEO', null=True)),
                ('fiscalyearend', models.DateField(db_column='FiscalYearEnd')),
                ('salarystatus', models.CharField(blank=True, db_column='SalaryStatus', max_length=50, null=True)),
                ('salary', models.FloatField(blank=True, db_column='Salary', null=True)),
                ('salarychange', models.FloatField(blank=True, db_column='SalaryChange', null=True)),
                ('bonus', models.FloatField(blank=True, db_column='Bonus', null=True)),
                ('bonuschange', models.FloatField(blank=True, db_column='BonusChange', null=True)),
                ('bonussalary', models.FloatField(blank=True, db_column='BonusSalary', null=True)),
                ('stockoptions', models.FloatField(blank=True, db_column='StockOptions', null=True)),
                ('stockoptionsvalue', models.FloatField(blank=True, db_column='StockOptionsValue', null=True)),
                ('othertotal', models.FloatField(blank=True, db_column='OtherTotal', null=True)),
                ('allothertotal', models.FloatField(blank=True, db_column='AllOtherTotal', null=True)),
                ('extratotal', models.FloatField(blank=True, db_column='ExtraTotal', null=True)),
                ('stockexpense', models.FloatField(blank=True, db_column='StockExpense', null=True)),
                ('restricted', models.FloatField(blank=True, db_column='Restricted', null=True)),
                ('performance', models.FloatField(blank=True, db_column='Performance', null=True)),
                ('longtermtotal', models.FloatField(blank=True, db_column='LongTermTotal', null=True)),
                ('longtermchange', models.FloatField(blank=True, db_column='LongTermChange', null=True)),
                ('optionsexercisablevalue', models.FloatField(blank=True, db_column='OptionsExercisableValue', null=True)),
                ('optionsunexercisablevalue', models.FloatField(blank=True, db_column='OptionsUnexercisableValue', null=True)),
                ('nr', models.IntegerField(blank=True, db_column='NR', null=True)),
                ('flag', models.IntegerField(blank=True, db_column='Flag', null=True)),
                ('totalltequitysct', models.FloatField(blank=True, db_column='TotalLTEquitySCT', null=True)),
                ('totalsb', models.FloatField(blank=True, db_column='TotalSB', null=True)),
                ('totalsbchange', models.FloatField(blank=True, db_column='TotalSBChange', null=True)),
                ('total', models.FloatField(blank=True, db_column='Total', null=True)),
                ('totalchange', models.FloatField(blank=True, db_column='TotalChange', null=True)),
                ('fullyear', models.IntegerField(blank=True, db_column='FullYear', null=True)),
                ('stockchange', models.FloatField(blank=True, db_column='StockChange', null=True)),
                ('stockaward', models.FloatField(blank=True, db_column='StockAward', null=True)),
                ('optionaward', models.FloatField(blank=True, db_column='OptionAward', null=True)),
                ('nonequityipc', models.FloatField(blank=True, db_column='NonEquityIPC', null=True)),
                ('pensionchange', models.FloatField(blank=True, db_column='PensionChange', null=True)),
                ('sharesvesting', models.FloatField(blank=True, db_column='SharesVesting', null=True)),
                ('ylabel', models.IntegerField(blank=True, db_column='YLabel', null=True)),
                ('sayonpay', models.FloatField(blank=True, db_column='SayOnPay', null=True)),
                ('ceopayratio', models.FloatField(blank=True, db_column='CEOPayRatio', null=True)),
                ('medianemployeepay', models.FloatField(blank=True, db_column='MedianEmployeePay', null=True)),
                ('footnotes', models.TextField(blank=True, db_column='Footnotes', null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
                ('officerid', models.ForeignKey(db_column='OfficerID', on_delete=django.db.models.deletion.DO_NOTHING, to='business_companies.Officer')),
            ],
            options={
                'verbose_name_plural': 'Officer Salaries',
                'db_table': 'Officer_Salaries',
                'managed': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='officersalary',
            unique_together={('officerid', 'publishyear')},
        ),
        migrations.AlterUniqueTogether(
            name='nonprofitsalary',
            unique_together={('officerid', 'publishyear')},
        ),
        migrations.AlterUniqueTogether(
            name='nonprofitfinances',
            unique_together={('coid', 'publishyear')},
        ),
        migrations.AlterUniqueTogether(
            name='finances',
            unique_together={('coid', 'publishyear')},
        ),
        migrations.AlterUniqueTogether(
            name='employees',
            unique_together={('coid', 'publishyear')},
        ),
    ]
