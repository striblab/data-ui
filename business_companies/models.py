# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from simple_history.models import HistoricalRecords
import datetime


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
        default=datetime.date.today,
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
        verbose_name='Type',
        help_text='General type of company.  This is an unstandardized field.',
        db_column='CompanyType',
        max_length=40,
        blank=True,
        null=True)
    category = models.CharField(
        verbose_name='Industry category',
        help_text='Industry category; (so far) mostly used for non-profit companies.',
        db_column='Category',
        max_length=200,
        blank=True,
        null=True)
    alpha = models.CharField(
        verbose_name='Sort name',
        help_text='The alphabetical sorting name used for this company.',
        db_column='Alpha',
        max_length=200,
        blank=True,
        null=True)
    seealso = models.CharField(
        verbose_name='See also',
        help_text='Descriptive reference for a related company.',
        db_column='SeeAlso',
        max_length=100,
        blank=True,
        null=True)
    seealsoid = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        verbose_name='See also company',
        help_text='The company ID to any related reference.',
        db_column='SeeAlsoID',
        blank=True,
        null=True)
    address1 = models.CharField(
        verbose_name='Address (line 1)',
        db_column='Address1',
        max_length=200,
        blank=True,
        null=True)
    address2 = models.CharField(
        verbose_name='Address (line 2)',
        db_column='Address2',
        max_length=200,
        blank=True,
        null=True)
    city = models.CharField(
        verbose_name='City',
        help_text='City for address.',
        db_column='City',
        max_length=100,
        blank=True,
        null=True)
    state = models.CharField(
        verbose_name='State',
        help_text='State for address; please use the postal abbreviation, such as "MN".',
        db_column='State',
        max_length=2,
        blank=True,
        null=True)
    zip = models.CharField(
        verbose_name='Zipcode',
        help_text='Zipcode for address.',
        db_column='Zip',
        max_length=20,
        blank=True,
        null=True)
    phone = models.CharField(
        verbose_name='Phone number',
        help_text='General phone number for company (see Contact Phone for specific contact phone number).',
        db_column='Phone',
        max_length=30,
        blank=True,
        null=True)
    fax = models.CharField(
        verbose_name='Fax number',
        help_text='General fax number for company.',
        db_column='Fax',
        max_length=30,
        blank=True,
        null=True)
    www = models.CharField(
        verbose_name='Website',
        help_text='URL of website for company.',
        db_column='WWW',
        max_length=200,
        blank=True,
        null=True)
    contact = models.CharField(
        verbose_name='Contact person',
        help_text='Name of main contact person.',
        db_column='Contact',
        max_length=200,
        blank=True,
        null=True)
    contactphone = models.CharField(
        verbose_name='Contact phone',
        help_text='Phone number of main contact person.',
        db_column='ContactPhone',
        max_length=30,
        blank=True,
        null=True)
    # TODO: EmailField
    contactemail = models.CharField(
        verbose_name='Contact email',
        help_text='Email address of main contact person.',
        db_column='ContactEmail',
        max_length=200,
        blank=True,
        null=True)
    description = models.TextField(
        verbose_name='Company description',
        help_text='Full description of company.',
        db_column='Description',
        blank=True,
        null=True)
    shortdesc = models.CharField(
        verbose_name='Short description',
        help_text='Short, one or two sentence, description of company.',
        db_column='ShortDesc',
        max_length=750,
        blank=True,
        null=True)
    companyhistory = models.TextField(
        verbose_name='Descriptive history',
        help_text='Descriptive history of company.',
        db_column='CompanyHistory',
        blank=True,
        null=True)
    founded = models.IntegerField(
        verbose_name='Year founded',
        help_text='Year company was founded.',
        db_column='Founded',
        blank=True,
        null=True)
    inc = models.IntegerField(
        verbose_name='Year incorporated',
        help_text='Year company was incorporated.',
        db_column='Inc',
        blank=True,
        null=True)
    incst = models.CharField(
        verbose_name='State incorporated',
        help_text='The state the company was incorporated in.  Please use the two character postal abbreviation, such as "MN".',
        db_column='IncSt',
        max_length=2,
        blank=True,
        null=True)
    stocksymbol = models.CharField(
        verbose_name='Stock symbol',
        help_text='Stock symbol used on exchanges.',
        db_column='StockSymbol',
        max_length=12,
        blank=True,
        null=True)
    exchange = models.CharField(
        verbose_name='Stock exchange',
        help_text='Primary exchange that the company is traded on.  This is an unstandardized field.',
        db_column='Exchange',
        max_length=50,
        blank=True,
        null=True)
    annualmeet = models.CharField(
        verbose_name='Annual meeting',
        help_text='About the annual meeting.',
        db_column='AnnualMeet',
        max_length=30,
        blank=True,
        null=True)
    fymonth = models.IntegerField(
        verbose_name='Fiscal year end month',
        help_text='The number month of the fiscal year end of the company.  Such as 1 for January.',
        db_column='FYMonth',
        blank=True,
        null=True)
    # TODO: This could/is handled by django
    enteredby = models.CharField(
        verbose_name='Data entered by',
        help_text='Who was the staff person that last entered this data.',
        db_column='EnteredBy', max_length=30, blank=True,
        null=True)  # Field name made lowercase.
    class_field = models.CharField(
        verbose_name='Class',
        help_text='An integer describing the class of the company.  (Unknown what this is)',
        db_column='Class',
        max_length=10,
        blank=True,
        null=True)
    notes = models.TextField(
        verbose_name='Internal notes',
        help_text='Any internal notes about this company.',
        db_column='Notes',
        blank=True,
        null=True)
    footnotes = models.TextField(
        verbose_name='Footnotes',
        help_text='Any footnotes to be used in publication.',
        db_column='Footnotes',
        blank=True,
        null=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        managed = True
        db_table = 'Companies'
        verbose_name_plural = 'Companies'
        ordering = ['name']


class Employees(BaseModel):
    id = models.AutoField(
        verbose_name='Employees ID',
        help_text='This is an auto incrementing ID that should not need to be manually created or updated.',
        db_column='ID',
        primary_key=True)
    added = models.DateField(
        verbose_name='Date added',
        help_text='The date this information was added.',
        default=datetime.date.today,
        db_column='Added')
    publishyear = models.IntegerField(
        verbose_name='Publish year',
        help_text='The calendar year this data will be published.',
        default=datetime.datetime.now().year,
        db_column='PublishYear')
    coid = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name='Company',
        help_text='The associated company with this data.',
        db_column='COID')
    parttime = models.IntegerField(
        verbose_name='Part-time',
        help_text='Number of part-time employees',
        db_column='PartTime',
        blank=True,
        null=True)
    fulltime = models.IntegerField(
        verbose_name='Full time',
        help_text='Number of full-time employees',
        db_column='FullTime',
        blank=True,
        null=True)
    union = models.IntegerField(
        verbose_name='Union',
        help_text='Number of union employees',
        db_column='Union',
        blank=True,
        null=True)
    total = models.IntegerField(
        verbose_name='Total',
        help_text='Total number of all employees.  This is the main number used in publication.',
        db_column='Total',
        blank=True,
        null=True)
    minnesota = models.IntegerField(
        verbose_name='MN employees',
        help_text='Number of employees in Minnesota',
        db_column='Minnesota',
        blank=True,
        null=True)
    footnotes = models.TextField(
        verbose_name='Footnotes',
        help_text='Any footnotes to be used in publication.',
        db_column='Footnotes',
        blank=True,
        null=True)
    notes = models.TextField(
        verbose_name='Internal notes',
        help_text='Any internal notes about this company.',
        db_column='Notes',
        blank=True,
        null=True)

    history = HistoricalRecords()

    def __str__(self):
        # Easier way to do this?
        return '%s employees: %s' % (
            '' if self.publishyear is None else self.publishyear,
            self.coid.name)

    class Meta:
        managed = True
        db_table = 'Employees'
        unique_together = (('coid', 'publishyear'), )
        verbose_name_plural = 'Employees'
        ordering = ['-publishyear', '-added', 'coid__name']


class Finances(BaseModel):
    id = models.AutoField(
        verbose_name='Financials ID',
        help_text='This is an auto incrementing ID that should not need to be manually created or updated.',
        db_column='ID',
        primary_key=True)
    coid = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name='Company',
        help_text='Company associated with this record.',
        db_column='COID')
    publishyear = models.IntegerField(
        verbose_name='Publish year',
        help_text='Year this data will be published.',
        default=datetime.datetime.now().year,
        db_column='PublishYear')
    customrank = models.IntegerField(
        verbose_name='Custom rank',
        help_text='(Not needed) Override ranking by revenue or other number.',
        db_column='CustomRank',
        blank=True,
        null=True)
    done = models.CharField(
        verbose_name='Done',
        help_text='(Not needed) Done for the year.',
        db_column='Done',
        max_length=10,
        blank=True,
        null=True)
    fye = models.DateField(
        verbose_name='Fiscal year end',
        help_text='(Not needed?  See maxoffye) Fiscal year end.',
        db_column='FYE',
        blank=True,
        null=True)
    maxoffye = models.DateField(
        verbose_name='Fiscal year end',
        help_text='Fiscal year end for the financial data.',
        db_column='MaxOfFYE',
        blank=True,
        null=True)
    ceo = models.CharField(
        verbose_name='CEO',
        help_text='(Not needed, see Officers tables) CEO of the year.',
        db_column='CEO',
        max_length=300,
        blank=True,
        null=True)
    category = models.CharField(
        verbose_name='Category',
        help_text='(Not needed, see Company tables) Industry category of company.',
        db_column='Category',
        max_length=300,
        blank=True,
        null=True)
    revenue = models.FloatField(
        verbose_name='Revenue',
        db_column='Revenue',
        blank=True,
        null=True)
    ati = models.FloatField(
        verbose_name='ATI',
        help_text='Unsure?.',
        db_column='ATI',
        blank=True,
        null=True)
    netincome = models.FloatField(
        verbose_name='Net income',
        db_column='NetIncome',
        blank=True,
        null=True)
    netincomebeforeextra = models.FloatField(
        verbose_name='Net income before extraordinary items',
        db_column='NetIncomeBeforeExtra',
        blank=True,
        null=True)
    earningspershare = models.FloatField(
        verbose_name='Earnings per share',
        db_column='EarningsPerShare',
        blank=True,
        null=True)
    totalassets = models.FloatField(
        verbose_name='Total assets',
        db_column='TotalAssets',
        blank=True,
        null=True)
    shareholdersequity = models.FloatField(
        verbose_name='Shareholders equity',
        db_column='ShareholdersEquity',
        blank=True,
        null=True)
    debt = models.FloatField(
        verbose_name='Debt',
        db_column='Debt',
        blank=True,
        null=True)
    shares = models.FloatField(
        verbose_name='Number of shares',
        db_column='Shares',
        blank=True,
        null=True)
    totalemployees = models.IntegerField(
        verbose_name='Total employees',
        help_text='(Not needed, see Employees tables) Number of total employees.',
        db_column='TotalEmployees',
        blank=True,
        null=True)
    mnemployees = models.IntegerField(
        verbose_name='MN employees',
        help_text='(Not needed, see Employees tables) Number of total employees in Minnesota.',
        db_column='MNEmployees',
        blank=True,
        null=True)
    marketcap = models.FloatField(
        verbose_name='Market cap',
        db_column='MarketCap',
        blank=True,
        null=True)
    empdate = models.DateField(
        verbose_name='Total employees date',
        help_text='(Not needed, see Employees tables) Date total employees was recorded.',
        db_column='EMPDate',
        blank=True,
        null=True)
    prevyearfye = models.DateField(
        help_text='(Not needed, see previous rows of data)',
        db_column='PrevYearFYE', blank=True,
        null=True)
    prevyearrevenue = models.FloatField(
        help_text='(Not needed, see previous rows of data)',
        db_column='PrevYearRevenue', blank=True,
        null=True)
    prevyearati = models.FloatField(
        help_text='(Not needed, see previous rows of data)',
        db_column='PrevYearATI', blank=True,
        null=True)
    prevyearnetincome = models.FloatField(
        help_text='(Not needed, see previous rows of data)',
        db_column='PrevYearNetIncome', blank=True,
        null=True)
    prevyearnetincomebeforeextra = models.FloatField(
        verbose_name='Previous year: Net income before extraordinary items',
        help_text='(Not needed, see previous rows of data)',
        db_column='PrevYearNetIncomeBE',
        blank=True,
        null=True)
    prevyearearnpershare = models.FloatField(
        help_text='(Not needed, see previous rows of data)',
        db_column='PrevYearEarnPerShare', blank=True,
        null=True)
    prevyeartotalassets = models.FloatField(
        help_text='(Not needed, see previous rows of data)',
        db_column='PrevYearTotalAssets', blank=True,
        null=True)
    prevyearshareequity = models.FloatField(
        help_text='(Not needed, see previous rows of data)',
        db_column='PrevYearShareEquity', blank=True,
        null=True)
    prevyeardebt = models.FloatField(
        help_text='(Not needed, see previous rows of data)',
        db_column='PrevYearDebt', blank=True,
        null=True)
    prevyearshares = models.FloatField(
        help_text='(Not needed, see previous rows of data)',
        db_column='PrevYearShares', blank=True,
        null=True)
    prevyeartotalemp = models.IntegerField(
        help_text='(Not needed, see previous rows of data)',
        db_column='PrevYearTotalEmp', blank=True,
        null=True)
    prevyearmnemp = models.IntegerField(
        help_text='(Not needed, see previous rows of data)',
        db_column='PrevYearMNEmp', blank=True,
        null=True)
    prevyearmarketcap = models.FloatField(
        help_text='(Not needed, see previous rows of data)',
        db_column='PrevYearMarketCap', blank=True,
        null=True)
    prevyearclose = models.FloatField(
        help_text='(Not needed, see previous rows of data)',
        db_column='PrevYearClose', blank=True,
        null=True)
    customrankrevenue = models.IntegerField(
        help_text='(Not needed, see previous rows of data)',
        db_column='CustomRankRevenue', blank=True,
        null=True)
    customrankprofit = models.IntegerField(
        help_text='(Not needed, see previous rows of data)',
        db_column='CustomRankProfit', blank=True,
        null=True)
    customrankassets = models.IntegerField(
        help_text='(Not needed, see previous rows of data)',
        db_column='CustomRankAssets', blank=True,
        null=True)
    customrankmarketcap = models.IntegerField(
        help_text='(Not needed, see previous rows of data)',
        db_column='CustomRankMarketCap', blank=True,
        null=True)
    customrankblend = models.IntegerField(
        help_text='(Not needed, see previous rows of data)',
        db_column='CustomRankBlend', blank=True,
        null=True)
    notes = models.TextField(
        verbose_name='Internal notes',
        help_text='Any internal notes about this company.',
        db_column='Notes',
        blank=True,
        null=True)
    footnotes = models.TextField(
        verbose_name='Footnotes',
        help_text='Any footnotes to be used in publication.',
        db_column='Footnotes',
        blank=True,
        null=True)

    history = HistoricalRecords()

    def __str__(self):
        # Easier way to do this?
        return '%s finances: %s' % (
            '' if self.publishyear is None else self.publishyear,
            self.coid.name)

    class Meta:
        managed = True
        db_table = 'Finances'
        unique_together = (('coid', 'publishyear'), )
        verbose_name_plural = 'Finances'
        ordering = ['-publishyear', '-revenue', 'coid__name']


class NonprofitFinances(BaseModel):
    id = models.AutoField(
        db_column='ID', primary_key=True)  # Field name made lowercase.
    coid = models.ForeignKey(
        Company, on_delete=models.CASCADE,
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
        'Officer', on_delete=models.CASCADE,
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
        verbose_name='Officer Salary ID',
        help_text='This is an auto incrementing ID that should not need to be manually created or updated.',
        db_column='ID',
        primary_key=True)
    officerid = models.ForeignKey(
        'Officer',
        on_delete=models.CASCADE,
        verbose_name='Officer',
        help_text='The related officer record.',
        db_column='OfficerID')
    added = models.DateField(
        verbose_name='Added',
        help_text='Date added.',
        db_column='Added')
    publishyear = models.IntegerField(
        verbose_name='Publish year',
        help_text='Year this record is used for publishing.',
        db_column='PublishYear')
    title = models.CharField(
        verbose_name='Officer title',
        help_text='(Deprecated, see Officer record)',
        db_column='Title',
        max_length=100,
        blank=True,
        null=True)
    ceo = models.IntegerField(
        verbose_name='Is CEO',
        help_text='(Deprecated, see Officer record) True (1) or False (0) on whether this is a CEO or not.',
        db_column='CEO',
        blank=True,
        null=True)
    fiscalyearend = models.DateField(
        verbose_name='Fiscal year end',
        help_text='Date of the fiscal year end.',
        db_column='FiscalYearEnd')
    salarystatus = models.CharField(
        verbose_name='Status',
        help_text='(Unsure what is used for)',
        db_column='SalaryStatus',
        max_length=50,
        blank=True,
        null=True)
    salary = models.FloatField(
        verbose_name='Base salary',
        help_text='Base salary for officer.',
        db_column='Salary',
        blank=True,
        null=True)
    salarychange = models.FloatField(
        help_text='(Deprecated, managed in previous records)',
        db_column='SalaryChange',
        blank=True,
        null=True)
    bonus = models.FloatField(
        verbose_name='Bonus',
        db_column='Bonus',
        blank=True,
        null=True)
    bonuschange = models.FloatField(
        help_text='(Deprecated, managed in previous records)',
        db_column='BonusChange',
        blank=True,
        null=True)
    bonussalary = models.FloatField(
        verbose_name='Subtotal: Bonus and salary',
        help_text='(Deprecated, calculated)',
        db_column='BonusSalary',
        blank=True,
        null=True)
    stockoptions = models.FloatField(
        verbose_name='Stock options',
        help_text='Number of stock options.',
        db_column='StockOptions',
        blank=True,
        null=True)
    stockoptionsvalue = models.FloatField(
        verbose_name='Value of stock options',
        help_text='Value of stock options.',
        db_column='StockOptionsValue',
        blank=True,
        null=True)
    othertotal = models.FloatField(
        verbose_name='Other total',
        help_text='(Unsure?)',
        db_column='OtherTotal',
        blank=True,
        null=True)
    allothertotal = models.FloatField(
        verbose_name='All other total',
        help_text='(Unsure?)',
        db_column='AllOtherTotal',
        blank=True,
        null=True)
    extratotal = models.FloatField(
        verbose_name='Extra total',
        help_text='(Unsure?)',
        db_column='ExtraTotal',
        blank=True,
        null=True)
    stockexpense = models.FloatField(
        verbose_name='Stock expenses',
        help_text='(Unsure?)',
        db_column='StockExpense',
         blank=True,
        null=True)
    restricted = models.FloatField(
        verbose_name='Restricted',
        help_text='(Unsure?)',
        db_column='Restricted',
        blank=True,
        null=True)
    performance = models.FloatField(
        verbose_name='Performance',
        help_text='(Unsure?)',
        db_column='Performance',
        blank=True,
        null=True)
    longtermtotal = models.FloatField(
        verbose_name='Long term total',
        help_text='(Unsure?)',
        db_column='LongTermTotal',
        blank=True,
        null=True)
    longtermchange = models.FloatField(
        help_text='(Deprecated, calculated)',
        db_column='LongTermChange',
        blank=True,
        null=True)
    optionsexercisablevalue = models.FloatField(
        verbose_name='Options exercisable value',
        db_column='OptionsExercisableValue',
        blank=True,
        null=True)
    optionsunexercisablevalue = models.FloatField(
        verbose_name='Options unexercisable value',
        db_column='OptionsUnexercisableValue',
        blank=True,
        null=True)
    nr = models.IntegerField(
        verbose_name='NR',
        help_text='(Unsure?)',
        db_column='NR',
        blank=True,
        null=True)
    flag = models.IntegerField(
        verbose_name='Flag',
        help_text='(Unsure?)',
        db_column='Flag',
        blank=True,
        null=True)
    totalltequitysct = models.FloatField(
        verbose_name='Total LT equity SCT',
        help_text='(Unsure?)',
        db_column='TotalLTEquitySCT',
        blank=True,
        null=True)
    totalsb = models.FloatField(
        verbose_name='Total SB',
        help_text='(Unsure?)',
        db_column='TotalSB',
        blank=True,
        null=True)
    totalsbchange = models.FloatField(
        help_text='(Deprecated, calculated)',
        db_column='TotalSBChange',
        blank=True,
        null=True)
    total = models.FloatField(
        verbose_name='Total pay',
        help_text='(Unsure?  Should be calculated?)',
        db_column='Total',
        blank=True,
        null=True)
    totalchange = models.FloatField(
        help_text='(Deprecated, calculated)',
        db_column='TotalChange',
        blank=True,
        null=True)
    fullyear = models.IntegerField(
        verbose_name='Is full year',
        help_text='True (1) or False (0) whether this data is for the full fiscal year.',
        db_column='FullYear',
        blank=True,
        null=True)
    stockchange = models.FloatField(
        help_text='(Deprecated, calculated)',
        db_column='StockChange',
        blank=True,
        null=True)
    stockaward = models.FloatField(
        verbose_name='Stock awards',
        help_text='(Unsure?)',
        db_column='StockAward',
        blank=True,
        null=True)
    optionaward = models.FloatField(
        verbose_name='Option awards',
        help_text='(Unsure?)',
        db_column='OptionAward',
        blank=True,
        null=True)
    nonequityipc = models.FloatField(
        verbose_name='Non-equity IPC',
        help_text='(Unsure?)',
        db_column='NonEquityIPC',
        blank=True,
        null=True)
    pensionchange = models.FloatField(
        help_text='(Deprecated, calculated)',
        db_column='PensionChange',
        blank=True,
        null=True)
    sharesvesting = models.FloatField(
        verbose_name='Shares vesting',
        help_text='(Unsure?)',
        db_column='SharesVesting',
        blank=True,
        null=True)
    ylabel = models.IntegerField(
        verbose_name='Y Label',
        help_text='(Unsure?)',
        db_column='YLabel',
        blank=True,
        null=True)
    sayonpay = models.FloatField(
        verbose_name='Say on pay',
        help_text='(Unsure?)',
        db_column='SayOnPay',
        blank=True,
        null=True)
    ceopayratio = models.FloatField(
        verbose_name='CEO pay ratio',
        help_text='Ratio of CEO to (average?) employee pay.',
        db_column='CEOPayRatio',
        blank=True,
        null=True)
    medianemployeepay = models.FloatField(
        verbose_name='Median employee pay',
        db_column='MedianEmployeePay',
        blank=True,
        null=True)
    footnotes = models.TextField(
        verbose_name='Footnotes',
        help_text='Any footnotes to be used in publication.',
        db_column='Footnotes',
        blank=True,
        null=True)
    notes = models.TextField(
        verbose_name='Internal notes',
        help_text='Any internal notes about this company.',
        db_column='Notes',
        blank=True,
        null=True)

    history = HistoricalRecords()

    def __str__(self):
        # Easier way to do this?
        return '%s salary: %s, %s, %s' % (
            '' if self.publishyear is None else self.publishyear,
            '' if self.officerid.last is None else self.officerid.last,
            '' if self.officerid.title is None else self.officerid.title,
            self.officerid.coid.name)

    class Meta:
        managed = True
        db_table = 'Officer_Salaries'
        unique_together = (('officerid', 'publishyear'), )
        verbose_name_plural = 'Officer Salaries'
        ordering = ['-publishyear', 'officerid__coid__name', 'officerid__last']


class Officer(BaseModel):
    id = models.AutoField(
        verbose_name='Officer ID',
        help_text='This is an auto incrementing ID that should not need to be manually created or updated.',
        db_column='ID',
        primary_key=True)
    coid = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name='Company',
        help_text='Company associated with this record.',
        db_column='COID')
    # TODO: Change to boolean field
    dropped = models.IntegerField(
        verbose_name='Is dropped',
        help_text='True (1) or False (0) on whether this person is no longer with company and should not show up in publication.',
        db_column='Dropped',
        blank=True,
        null=True)
    salut = models.CharField(
        verbose_name='Salut',
        help_text='Name prefix',
        db_column='Salut', max_length=50, blank=True,
        null=True)
    first = models.CharField(
        verbose_name='First name',
        db_column='First',
        max_length=200,
        blank=True,
        null=True)
    middle = models.CharField(
        verbose_name='Middle name',
        db_column='Middle',
        max_length=50,
        blank=True,
        null=True)
    last = models.CharField(
        verbose_name='Last name',
        db_column='Last',
        max_length=200)
    lineage = models.CharField(
        verbose_name='Lineage suffix',
        help_text='Name suffix or lineage.',
        db_column='Lineage',
        max_length=50,
        blank=True,
        null=True)
    degree = models.CharField(
        verbose_name='Degree suffix',
        help_text='Degree suffix such as "M.D.".',
        db_column='Degree',
        max_length=50,
        blank=True,
        null=True)
    gender = models.CharField(
        verbose_name='Gender',
        help_text='Gender as either M, F, or blank',
        db_column='Gender',
        max_length=50,
        blank=True,
        null=True)
    race = models.CharField(
        verbose_name='Race',
        help_text='This field is not standardized or consistenly used so is probably not a reliable field for publication.',
        db_column='Race',
        max_length=50,
        blank=True,
        null=True)
    title = models.CharField(
        verbose_name='Title',
        help_text='The current title of the officer.',
        db_column='Title',
        max_length=110,
        blank=True,
        null=True)
    director = models.IntegerField(
        verbose_name='Is director',
        help_text='True (1) or False (0) whether this person is a director.',
        db_column='Director',
        blank=True,
        null=True)
    birthday = models.DateField(
        verbose_name='Birthday',
        db_column='Birthday',
        blank=True,
        null=True)
    tenure = models.CharField(
        verbose_name='Tenure',
        help_text='Year this officer joined the company.',
        db_column='Tenure',
        max_length=200,
        blank=True,
        null=True)
    phone = models.CharField(
        verbose_name='Phone number',
        db_column='Phone',
        max_length=30,
        blank=True,
        null=True)
    email = models.CharField(
        verbose_name='Email',
        db_column='Email',
        max_length=200,
        blank=True,
        null=True)
    twitter = models.CharField(
        verbose_name='Twitter handle',
        db_column='Twitter',
        max_length=200,
        blank=True,
        null=True)
    footnotes = models.TextField(
        verbose_name='Footnotes',
        help_text='Any footnotes to be used in publication.',
        db_column='Footnotes',
        blank=True,
        null=True)
    notes = models.TextField(
        verbose_name='Internal notes',
        help_text='Any internal notes about this company.',
        db_column='Notes',
        blank=True,
        null=True)

    history = HistoricalRecords()

    def __str__(self):
        # Easier way to do this?
        return '%s %s %s, %s, %s' % (
            '' if self.first is None else self.first,
            '' if self.middle is None else self.middle,
            self.last,
            '' if self.title is None else self.title,
            self.coid.name)

    class Meta:
        managed = True
        db_table = 'Officers'
        verbose_name_plural = 'Officers'
        ordering = ['dropped', 'coid__name', 'last']
