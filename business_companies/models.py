# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from simple_history.models import HistoricalRecords


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Company(BaseModel):
    coid = models.CharField(
        verbose_name='Company ID',
        help_text='Alphanumeric unique identifier for each company.',
        db_column='COID',
        primary_key=True,
        max_length=100)
    added = models.DateField(
        verbose_name='Date added',
        help_text='Date this company was added.',
        blank=True,
        auto_now_add=True,
        db_column='Added')
    irsno = models.CharField(
        verbose_name='IRS number',
        db_column='IRSNo',
        max_length=100,
        blank=True,
        null=True)
    name = models.CharField(
        verbose_name='Name',
        help_text='Full, official name of company',
        db_column='Company',
        max_length=200,
        blank=True,
        null=True)
    companytype = models.CharField(
        db_column='CompanyType', max_length=40, blank=True,
        null=True)  # Field name made lowercase.
    category = models.CharField(
        db_column='Category', max_length=200, blank=True,
        null=True)  # Field name made lowercase.
    alpha = models.CharField(
        db_column='Alpha', max_length=200, blank=True,
        null=True)  # Field name made lowercase.
    seealso = models.CharField(
        db_column='SeeAlso', max_length=100, blank=True,
        null=True)  # Field name made lowercase.
    seealsoid = models.ForeignKey(
        'self',
        models.DO_NOTHING,
        db_column='SeeAlsoID',
        blank=True,
        null=True)  # Field name made lowercase.
    address1 = models.CharField(
        db_column='Address1', max_length=200, blank=True,
        null=True)  # Field name made lowercase.
    address2 = models.CharField(
        db_column='Address2', max_length=200, blank=True,
        null=True)  # Field name made lowercase.
    city = models.CharField(
        db_column='City', max_length=100, blank=True,
        null=True)  # Field name made lowercase.
    state = models.CharField(
        db_column='State', max_length=2, blank=True,
        null=True)  # Field name made lowercase.
    zip = models.CharField(
        db_column='Zip', max_length=20, blank=True,
        null=True)  # Field name made lowercase.
    phone = models.CharField(
        db_column='Phone', max_length=30, blank=True,
        null=True)  # Field name made lowercase.
    fax = models.CharField(
        db_column='Fax', max_length=30, blank=True,
        null=True)  # Field name made lowercase.
    www = models.CharField(
        db_column='WWW', max_length=200, blank=True,
        null=True)  # Field name made lowercase.
    contact = models.CharField(
        db_column='Contact', max_length=200, blank=True,
        null=True)  # Field name made lowercase.
    contactphone = models.CharField(
        db_column='ContactPhone', max_length=30, blank=True,
        null=True)  # Field name made lowercase.
    contactemail = models.CharField(
        db_column='ContactEmail', max_length=200, blank=True,
        null=True)  # Field name made lowercase.
    description = models.TextField(
        db_column='Description', blank=True,
        null=True)  # Field name made lowercase.
    shortdesc = models.CharField(
        db_column='ShortDesc', max_length=750, blank=True,
        null=True)  # Field name made lowercase.
    history = models.TextField(
        db_column='History', blank=True,
        null=True)  # Field name made lowercase.
    founded = models.IntegerField(
        db_column='Founded', blank=True,
        null=True)  # Field name made lowercase.
    inc = models.IntegerField(
        db_column='Inc', blank=True, null=True)  # Field name made lowercase.
    incst = models.CharField(
        db_column='IncSt', max_length=2, blank=True,
        null=True)  # Field name made lowercase.
    stocksymbol = models.CharField(
        db_column='StockSymbol', max_length=12, blank=True,
        null=True)  # Field name made lowercase.
    exchange = models.CharField(
        db_column='Exchange', max_length=50, blank=True,
        null=True)  # Field name made lowercase.
    annualmeet = models.CharField(
        db_column='AnnualMeet', max_length=30, blank=True,
        null=True)  # Field name made lowercase.
    fymonth = models.IntegerField(
        db_column='FYMonth', blank=True,
        null=True)  # Field name made lowercase.
    enteredby = models.CharField(
        db_column='EnteredBy', max_length=30, blank=True,
        null=True)  # Field name made lowercase.
    class_field = models.CharField(
        db_column='Class', max_length=10, blank=True, null=True
    )  # Field name made lowercase. Field renamed because it was a Python reserved word.
    notes = models.TextField(
        db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    footnotes = models.TextField(
        db_column='Footnotes', blank=True,
        null=True)  # Field name made lowercase.

    history = HistoricalRecords()

    class Meta:
        managed = True
        db_table = 'Companies'
        verbose_name_plural = 'Companies'


class Employees(BaseModel):
    id = models.AutoField(
        db_column='ID', primary_key=True)  # Field name made lowercase.
    added = models.DateField(db_column='Added')  # Field name made lowercase.
    publishyear = models.IntegerField(
        db_column='PublishYear')  # Field name made lowercase.
    coid = models.ForeignKey(
        Company, models.DO_NOTHING,
        db_column='COID')  # Field name made lowercase.
    parttime = models.IntegerField(
        db_column='PartTime', blank=True,
        null=True)  # Field name made lowercase.
    fulltime = models.IntegerField(
        db_column='FullTime', blank=True,
        null=True)  # Field name made lowercase.
    union = models.IntegerField(
        db_column='Union', blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(
        db_column='Total', blank=True, null=True)  # Field name made lowercase.
    minnesota = models.IntegerField(
        db_column='Minnesota', blank=True,
        null=True)  # Field name made lowercase.
    footnotes = models.TextField(
        db_column='Footnotes', blank=True,
        null=True)  # Field name made lowercase.
    notes = models.TextField(
        db_column='Notes', blank=True, null=True)  # Field name made lowercase.

    history = HistoricalRecords()

    class Meta:
        managed = True
        db_table = 'Employees'
        unique_together = (('coid', 'publishyear'), )
        verbose_name_plural = 'Employees'


class Finances(BaseModel):
    id = models.AutoField(
        db_column='ID', primary_key=True)  # Field name made lowercase.
    coid = models.ForeignKey(
        Company, models.DO_NOTHING,
        db_column='COID')  # Field name made lowercase.
    publishyear = models.IntegerField(
        db_column='PublishYear')  # Field name made lowercase.
    customrank = models.IntegerField(
        db_column='CustomRank', blank=True,
        null=True)  # Field name made lowercase.
    done = models.CharField(
        db_column='Done', max_length=10, blank=True,
        null=True)  # Field name made lowercase.
    fye = models.DateField(
        db_column='FYE', blank=True, null=True)  # Field name made lowercase.
    maxoffye = models.DateField(
        db_column='MaxOfFYE', blank=True,
        null=True)  # Field name made lowercase.
    ceo = models.CharField(
        db_column='CEO', max_length=300, blank=True,
        null=True)  # Field name made lowercase.
    category = models.CharField(
        db_column='Category', max_length=300, blank=True,
        null=True)  # Field name made lowercase.
    revenue = models.FloatField(
        db_column='Revenue', blank=True,
        null=True)  # Field name made lowercase.
    ati = models.FloatField(
        db_column='ATI', blank=True, null=True)  # Field name made lowercase.
    netincome = models.FloatField(
        db_column='NetIncome', blank=True,
        null=True)  # Field name made lowercase.
    earningspershare = models.FloatField(
        db_column='EarningsPerShare', blank=True,
        null=True)  # Field name made lowercase.
    totalassets = models.FloatField(
        db_column='TotalAssets', blank=True,
        null=True)  # Field name made lowercase.
    shareholdersequity = models.FloatField(
        db_column='ShareholdersEquity', blank=True,
        null=True)  # Field name made lowercase.
    debt = models.FloatField(
        db_column='Debt', blank=True, null=True)  # Field name made lowercase.
    shares = models.FloatField(
        db_column='Shares', blank=True,
        null=True)  # Field name made lowercase.
    totalemployees = models.IntegerField(
        db_column='TotalEmployees', blank=True,
        null=True)  # Field name made lowercase.
    mnemployees = models.IntegerField(
        db_column='MNEmployees', blank=True,
        null=True)  # Field name made lowercase.
    marketcap = models.FloatField(
        db_column='MarketCap', blank=True,
        null=True)  # Field name made lowercase.
    empdate = models.DateField(
        db_column='EMPDate', blank=True,
        null=True)  # Field name made lowercase.
    prevyearfye = models.DateField(
        db_column='PrevYearFYE', blank=True,
        null=True)  # Field name made lowercase.
    prevyearrevenue = models.FloatField(
        db_column='PrevYearRevenue', blank=True,
        null=True)  # Field name made lowercase.
    prevyearati = models.FloatField(
        db_column='PrevYearATI', blank=True,
        null=True)  # Field name made lowercase.
    prevyearnetincome = models.FloatField(
        db_column='PrevYearNetIncome', blank=True,
        null=True)  # Field name made lowercase.
    prevyearearnpershare = models.FloatField(
        db_column='PrevYearEarnPerShare', blank=True,
        null=True)  # Field name made lowercase.
    prevyeartotalassets = models.FloatField(
        db_column='PrevYearTotalAssets', blank=True,
        null=True)  # Field name made lowercase.
    prevyearshareequity = models.FloatField(
        db_column='PrevYearShareEquity', blank=True,
        null=True)  # Field name made lowercase.
    prevyeardebt = models.FloatField(
        db_column='PrevYearDebt', blank=True,
        null=True)  # Field name made lowercase.
    prevyearshares = models.FloatField(
        db_column='PrevYearShares', blank=True,
        null=True)  # Field name made lowercase.
    prevyeartotalemp = models.IntegerField(
        db_column='PrevYearTotalEmp', blank=True,
        null=True)  # Field name made lowercase.
    prevyearmnemp = models.IntegerField(
        db_column='PrevYearMNEmp', blank=True,
        null=True)  # Field name made lowercase.
    prevyearmarketcap = models.FloatField(
        db_column='PrevYearMarketCap', blank=True,
        null=True)  # Field name made lowercase.
    prevyearclose = models.FloatField(
        db_column='PrevYearClose', blank=True,
        null=True)  # Field name made lowercase.
    customrankrevenue = models.IntegerField(
        db_column='CustomRankRevenue', blank=True,
        null=True)  # Field name made lowercase.
    customrankprofit = models.IntegerField(
        db_column='CustomRankProfit', blank=True,
        null=True)  # Field name made lowercase.
    customrankassets = models.IntegerField(
        db_column='CustomRankAssets', blank=True,
        null=True)  # Field name made lowercase.
    customrankmarketcap = models.IntegerField(
        db_column='CustomRankMarketCap', blank=True,
        null=True)  # Field name made lowercase.
    customrankblend = models.IntegerField(
        db_column='CustomRankBlend', blank=True,
        null=True)  # Field name made lowercase.
    notes = models.TextField(
        db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    footnotes = models.TextField(
        db_column='Footnotes', blank=True,
        null=True)  # Field name made lowercase.

    history = HistoricalRecords()

    class Meta:
        managed = True
        db_table = 'Finances'
        unique_together = (('coid', 'publishyear'), )
        verbose_name_plural = 'Finances'


class NonprofitFinances(BaseModel):
    id = models.AutoField(
        db_column='ID', primary_key=True)  # Field name made lowercase.
    coid = models.ForeignKey(
        Company, models.DO_NOTHING,
        db_column='COID')  # Field name made lowercase.
    added = models.DateField(db_column='Added')  # Field name made lowercase.
    publishyear = models.IntegerField(
        db_column='PublishYear')  # Field name made lowercase.
    status = models.CharField(
        db_column='Status', max_length=50, blank=True,
        null=True)  # Field name made lowercase.
    fiscalyearend = models.DateField(
        db_column='FiscalYearEnd')  # Field name made lowercase.
    annualreportdate = models.DateField(
        db_column='AnnualReportDate')  # Field name made lowercase.
    source = models.CharField(
        db_column='Source', max_length=512, blank=True,
        null=True)  # Field name made lowercase.
    contribgrants = models.FloatField(
        db_column='ContribGrants', blank=True,
        null=True)  # Field name made lowercase.
    revenue = models.FloatField(
        db_column='Revenue', blank=True,
        null=True)  # Field name made lowercase.
    expenses = models.FloatField(
        db_column='Expenses', blank=True,
        null=True)  # Field name made lowercase.
    excess = models.FloatField(
        db_column='Excess', blank=True,
        null=True)  # Field name made lowercase.
    programservicerevenue = models.FloatField(
        db_column='ProgramServiceRevenue', blank=True,
        null=True)  # Field name made lowercase.
    investgainslosses = models.FloatField(
        db_column='InvestGainsLosses', blank=True,
        null=True)  # Field name made lowercase.
    programserviceexpense = models.FloatField(
        db_column='ProgramServiceExpense', blank=True,
        null=True)  # Field name made lowercase.
    managementgeneralexpenses = models.FloatField(
        db_column='ManagementGeneralExpenses', blank=True,
        null=True)  # Field name made lowercase.
    fundraisingexpenses = models.FloatField(
        db_column='FundraisingExpenses', blank=True,
        null=True)  # Field name made lowercase.
    eoybalance = models.FloatField(
        db_column='EOYBalance', blank=True,
        null=True)  # Field name made lowercase.
    inputsource = models.CharField(
        db_column='InputSource', max_length=512, blank=True,
        null=True)  # Field name made lowercase.
    notes = models.TextField(
        db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    footnotes = models.TextField(
        db_column='Footnotes', blank=True,
        null=True)  # Field name made lowercase.

    history = HistoricalRecords()

    class Meta:
        managed = True
        db_table = 'NonProfit_Finances'
        unique_together = (('coid', 'publishyear'), )
        verbose_name_plural = 'NonProfit Finances'


class NonprofitSalary(BaseModel):
    id = models.AutoField(
        db_column='ID', primary_key=True)  # Field name made lowercase.
    officerid = models.ForeignKey(
        'Officer', models.DO_NOTHING,
        db_column='OfficerID')  # Field name made lowercase.
    added = models.DateField(db_column='Added')  # Field name made lowercase.
    publishyear = models.IntegerField(
        db_column='PublishYear')  # Field name made lowercase.
    salarystatus = models.CharField(
        db_column='SalaryStatus', max_length=50, blank=True,
        null=True)  # Field name made lowercase.
    fiscalyearend = models.DateField(
        db_column='FiscalYearEnd')  # Field name made lowercase.
    fiscalyearnbr = models.IntegerField(
        db_column='FiscalYearNBR', blank=True,
        null=True)  # Field name made lowercase.
    salary = models.FloatField(
        db_column='Salary', blank=True,
        null=True)  # Field name made lowercase.
    benefit = models.FloatField(
        db_column='Benefit', blank=True,
        null=True)  # Field name made lowercase.
    other = models.FloatField(
        db_column='Other', blank=True, null=True)  # Field name made lowercase.
    bonus = models.FloatField(
        db_column='Bonus', blank=True, null=True)  # Field name made lowercase.
    deferred = models.FloatField(
        db_column='Deferred', blank=True,
        null=True)  # Field name made lowercase.
    total = models.FloatField(
        db_column='Total', blank=True, null=True)  # Field name made lowercase.
    footnotes = models.TextField(
        db_column='Footnotes', blank=True,
        null=True)  # Field name made lowercase.
    notes = models.TextField(
        db_column='Notes', blank=True, null=True)  # Field name made lowercase.

    history = HistoricalRecords()

    class Meta:
        managed = True
        db_table = 'NonProfit_Salaries'
        unique_together = (('officerid', 'publishyear'), )
        verbose_name_plural = 'NonProfit Salaries'


class OfficerSalary(BaseModel):
    id = models.AutoField(
        db_column='ID', primary_key=True)  # Field name made lowercase.
    officerid = models.ForeignKey(
        'Officer', models.DO_NOTHING,
        db_column='OfficerID')  # Field name made lowercase.
    added = models.DateField(db_column='Added')  # Field name made lowercase.
    publishyear = models.IntegerField(
        db_column='PublishYear')  # Field name made lowercase.
    title = models.CharField(
        db_column='Title', max_length=100, blank=True,
        null=True)  # Field name made lowercase.
    ceo = models.IntegerField(
        db_column='CEO', blank=True, null=True)  # Field name made lowercase.
    fiscalyearend = models.DateField(
        db_column='FiscalYearEnd')  # Field name made lowercase.
    salarystatus = models.CharField(
        db_column='SalaryStatus', max_length=50, blank=True,
        null=True)  # Field name made lowercase.
    salary = models.FloatField(
        db_column='Salary', blank=True,
        null=True)  # Field name made lowercase.
    salarychange = models.FloatField(
        db_column='SalaryChange', blank=True,
        null=True)  # Field name made lowercase.
    bonus = models.FloatField(
        db_column='Bonus', blank=True, null=True)  # Field name made lowercase.
    bonuschange = models.FloatField(
        db_column='BonusChange', blank=True,
        null=True)  # Field name made lowercase.
    bonussalary = models.FloatField(
        db_column='BonusSalary', blank=True,
        null=True)  # Field name made lowercase.
    stockoptions = models.FloatField(
        db_column='StockOptions', blank=True,
        null=True)  # Field name made lowercase.
    stockoptionsvalue = models.FloatField(
        db_column='StockOptionsValue', blank=True,
        null=True)  # Field name made lowercase.
    othertotal = models.FloatField(
        db_column='OtherTotal', blank=True,
        null=True)  # Field name made lowercase.
    allothertotal = models.FloatField(
        db_column='AllOtherTotal', blank=True,
        null=True)  # Field name made lowercase.
    extratotal = models.FloatField(
        db_column='ExtraTotal', blank=True,
        null=True)  # Field name made lowercase.
    stockexpense = models.FloatField(
        db_column='StockExpense', blank=True,
        null=True)  # Field name made lowercase.
    restricted = models.FloatField(
        db_column='Restricted', blank=True,
        null=True)  # Field name made lowercase.
    performance = models.FloatField(
        db_column='Performance', blank=True,
        null=True)  # Field name made lowercase.
    longtermtotal = models.FloatField(
        db_column='LongTermTotal', blank=True,
        null=True)  # Field name made lowercase.
    longtermchange = models.FloatField(
        db_column='LongTermChange', blank=True,
        null=True)  # Field name made lowercase.
    optionsexercisablevalue = models.FloatField(
        db_column='OptionsExercisableValue', blank=True,
        null=True)  # Field name made lowercase.
    optionsunexercisablevalue = models.FloatField(
        db_column='OptionsUnexercisableValue', blank=True,
        null=True)  # Field name made lowercase.
    nr = models.IntegerField(
        db_column='NR', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(
        db_column='Flag', blank=True, null=True)  # Field name made lowercase.
    totalltequitysct = models.FloatField(
        db_column='TotalLTEquitySCT', blank=True,
        null=True)  # Field name made lowercase.
    totalsb = models.FloatField(
        db_column='TotalSB', blank=True,
        null=True)  # Field name made lowercase.
    totalsbchange = models.FloatField(
        db_column='TotalSBChange', blank=True,
        null=True)  # Field name made lowercase.
    total = models.FloatField(
        db_column='Total', blank=True, null=True)  # Field name made lowercase.
    totalchange = models.FloatField(
        db_column='TotalChange', blank=True,
        null=True)  # Field name made lowercase.
    fullyear = models.IntegerField(
        db_column='FullYear', blank=True,
        null=True)  # Field name made lowercase.
    stockchange = models.FloatField(
        db_column='StockChange', blank=True,
        null=True)  # Field name made lowercase.
    stockaward = models.FloatField(
        db_column='StockAward', blank=True,
        null=True)  # Field name made lowercase.
    optionaward = models.FloatField(
        db_column='OptionAward', blank=True,
        null=True)  # Field name made lowercase.
    nonequityipc = models.FloatField(
        db_column='NonEquityIPC', blank=True,
        null=True)  # Field name made lowercase.
    pensionchange = models.FloatField(
        db_column='PensionChange', blank=True,
        null=True)  # Field name made lowercase.
    sharesvesting = models.FloatField(
        db_column='SharesVesting', blank=True,
        null=True)  # Field name made lowercase.
    ylabel = models.IntegerField(
        db_column='YLabel', blank=True,
        null=True)  # Field name made lowercase.
    sayonpay = models.FloatField(
        db_column='SayOnPay', blank=True,
        null=True)  # Field name made lowercase.
    ceopayratio = models.FloatField(
        db_column='CEOPayRatio', blank=True,
        null=True)  # Field name made lowercase.
    medianemployeepay = models.FloatField(
        db_column='MedianEmployeePay', blank=True,
        null=True)  # Field name made lowercase.
    footnotes = models.TextField(
        db_column='Footnotes', blank=True,
        null=True)  # Field name made lowercase.
    notes = models.TextField(
        db_column='Notes', blank=True, null=True)  # Field name made lowercase.

    history = HistoricalRecords()

    class Meta:
        managed = True
        db_table = 'Officer_Salaries'
        unique_together = (('officerid', 'publishyear'), )
        verbose_name_plural = 'Officer Salaries'


class Officer(BaseModel):
    id = models.AutoField(
        db_column='ID', primary_key=True)  # Field name made lowercase.
    coid = models.ForeignKey(
        Company, models.DO_NOTHING,
        db_column='COID')  # Field name made lowercase.
    dropped = models.IntegerField(
        db_column='Dropped', blank=True,
        null=True)  # Field name made lowercase.
    salut = models.CharField(
        db_column='Salut', max_length=50, blank=True,
        null=True)  # Field name made lowercase.
    first = models.CharField(
        db_column='First', max_length=200, blank=True,
        null=True)  # Field name made lowercase.
    middle = models.CharField(
        db_column='Middle', max_length=50, blank=True,
        null=True)  # Field name made lowercase.
    last = models.CharField(
        db_column='Last', max_length=200)  # Field name made lowercase.
    lineage = models.CharField(
        db_column='Lineage', max_length=50, blank=True,
        null=True)  # Field name made lowercase.
    degree = models.CharField(
        db_column='Degree', max_length=50, blank=True,
        null=True)  # Field name made lowercase.
    gender = models.CharField(
        db_column='Gender', max_length=50, blank=True,
        null=True)  # Field name made lowercase.
    race = models.CharField(
        db_column='Race', max_length=50, blank=True,
        null=True)  # Field name made lowercase.
    title = models.CharField(
        db_column='Title', max_length=110, blank=True,
        null=True)  # Field name made lowercase.
    director = models.IntegerField(
        db_column='Director', blank=True,
        null=True)  # Field name made lowercase.
    birthday = models.DateField(
        db_column='Birthday', blank=True,
        null=True)  # Field name made lowercase.
    tenure = models.CharField(
        db_column='Tenure', max_length=200, blank=True,
        null=True)  # Field name made lowercase.
    phone = models.CharField(
        db_column='Phone', max_length=30, blank=True,
        null=True)  # Field name made lowercase.
    email = models.CharField(
        db_column='Email', max_length=200, blank=True,
        null=True)  # Field name made lowercase.
    twitter = models.CharField(
        db_column='Twitter', max_length=200, blank=True,
        null=True)  # Field name made lowercase.
    footnotes = models.TextField(
        db_column='Footnotes', blank=True,
        null=True)  # Field name made lowercase.
    notes = models.TextField(
        db_column='Notes', blank=True, null=True)  # Field name made lowercase.

    history = HistoricalRecords()

    class Meta:
        managed = True
        db_table = 'Officers'
        verbose_name_plural = 'Officers'
