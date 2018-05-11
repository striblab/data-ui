from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Company, Employees, Finances, NonprofitFinances, NonprofitSalary, OfficerSalary, Officer

# Referenence
# https://docs.djangoproject.com/en/2.0/ref/contrib/admin/


# Customize inline admin interfaces
# https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#inlinemodeladmin-objects
class CompanyInline(admin.TabularInline):
    model = Company
    extra = 0
    show_change_link = True
    fields = ('coid', 'name')


class EmployeesInline(admin.TabularInline):
    model = Employees
    extra = 0
    show_change_link = True
    fields = ('added', 'publishyear', 'parttime', 'fulltime', 'union', 'total',
              'minnesota')


class OfficerInline(admin.TabularInline):
    model = Officer
    extra = 0
    show_change_link = True
    fields = ('dropped', 'title', 'first', 'last')


class FinancesInline(admin.TabularInline):
    model = Finances
    extra = 0
    show_change_link = True
    fields = ('publishyear', 'revenue', 'netincomebeforeextra', 'netincome',
              'marketcap', 'totalassets')


class OfficerSalaryInline(admin.TabularInline):
    model = OfficerSalary
    extra = 0
    show_change_link = True
    fields = ('publishyear', 'title', 'salary', 'total')


# Customize main admin interface for Company
@admin.register(Company)
class CompanyAdmin(SimpleHistoryAdmin):
    #date_hierarchy = 'modified_date'
    list_display = ('coid', 'name', 'stocksymbol', 'category', 'companytype',
                    'shortdesc', 'modified_date')
    list_filter = ('category', 'companytype')
    search_fields = ['coid', 'name', 'stocksymbol']
    autocomplete_fields = ['seealsoid']
    inlines = [EmployeesInline, OfficerInline, FinancesInline]
    readonly_fields = ('created_date', 'modified_date')
    fieldsets = (
        (None, {
            'fields': ('coid', 'added', 'name', 'alpha', 'irsno',
                       'stocksymbol', 'exchange')
        }),
        (
            'Grouping',
            {
                #'classes': ('collapse',),
                'fields': ('companytype', 'category'),
            }),
        ('About', {
            'fields':
            ('description', 'companyhistory', 'shortdesc', 'founded', 'inc',
             'incst', 'footnotes', 'annualmeet', 'fymonth', 'class_field'),
        }),
        ('References', {
            'fields': ('seealso', 'seealsoid'),
        }),
        ('Address', {
            'fields': ('address1', 'address2', 'city', 'state', 'zip', 'phone',
                       'fax', 'www'),
        }),
        ('Main contact', {
            'fields': ('contact', 'contactphone', 'contactemail'),
        }),
        ('Internal', {
            'fields': ('notes', 'enteredby', 'created_date', 'modified_date'),
        }),
    )


@admin.register(Employees)
class EmployeesAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'coid', 'publishyear', 'added', 'total',
                    'modified_date')
    list_filter = ('publishyear', )
    search_fields = ['id', 'coid__name', 'publishyear']
    autocomplete_fields = ['coid']
    readonly_fields = ('id', 'created_date', 'modified_date')
    fieldsets = (
        (None, {
            'fields': ('id', 'coid', 'added', 'publishyear')
        }),
        ('Employees', {
            'fields': ('total', 'parttime', 'fulltime', 'union', 'minnesota'),
        }),
        ('About', {
            'fields': ('footnotes', ),
        }),
        ('Internal', {
            'fields': ('notes', 'created_date', 'modified_date'),
        }),
    )


@admin.register(Finances)
class FinancesAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'coid', 'publishyear', 'maxoffye', 'revenue',
                    'netincomebeforeextra', 'netincome', 'marketcap',
                    'totalassets', 'modified_date')
    list_filter = ('publishyear', )
    search_fields = ['id', 'coid__name', 'publishyear']
    autocomplete_fields = ['coid']
    readonly_fields = ('id', 'created_date', 'modified_date')
    fieldsets = (
        (None, {
            'fields': ('id', 'coid', 'publishyear', 'maxoffye')
        }),
        ('Financials', {
            'description':
            'All numbers should be full, base-10 values.  For example 4 billion needs to be 4000000000.',
            'fields': ('revenue', 'ati', 'netincomebeforeextra', 'netincome',
                       'earningspershare', 'totalassets', 'shareholdersequity',
                       'debt', 'shares', 'marketcap'),
        }),
        ('About', {
            'fields': ('footnotes', ),
        }),
        ('Internal', {
            'fields': ('notes', 'created_date', 'modified_date'),
        }),
        ('Other', {
            'classes': ('collapse', ),
            'fields': ('ceo', 'category', 'customrank', 'done'),
        }),
    )


@admin.register(Officer)
class OfficerAdmin(SimpleHistoryAdmin):
    # Using title from salary table
    list_display = ('id', 'coid', 'dropped', 'last', 'first', 'modified_date')
    list_filter = ('dropped', )
    search_fields = ['id', 'coid__name', 'last', 'first']
    autocomplete_fields = ['coid']
    inlines = [OfficerSalaryInline]
    readonly_fields = ('id', 'created_date', 'modified_date')
    fieldsets = (
        (None, {
            'fields': ('id', 'coid', 'dropped')
        }),
        ('Name', {
            'fields': ('salut', 'first', 'middle', 'last', 'lineage',
                       'degree'),
        }),
        ('Demographics', {
            'fields': ('gender', 'race', 'birthday'),
        }),
        ('Contact', {
            'fields': ('phone', 'email', 'twitter'),
        }),
        ('About', {
            'fields': ('footnotes', ),
        }),
        ('Internal', {
            'fields': ('notes', 'created_date', 'modified_date'),
        }),
        ('Other', {
            'classes': ('collapse', ),
            'fields': ('title', 'director', 'tenure'),
        }),
    )


@admin.register(OfficerSalary)
class OfficerSalaryAdmin(SimpleHistoryAdmin):
    list_display = ('id', 'publishyear', 'officerid', 'title', 'salary',
                    'modified_date')
    list_filter = ('publishyear', )
    search_fields = [
        'publishyear', 'officerid__coid__name', 'title', 'officerid__last',
        'officerid__first'
    ]
    autocomplete_fields = ['officerid']
    #inlines = [OfficerInline]
    readonly_fields = ('id', 'created_date', 'modified_date')
    fieldsets = (
        (None, {
            'fields': ('id', 'officerid', 'added', 'publishyear',
                       'fiscalyearend', 'salarystatus', 'fullyear')
        }),
        ('Officer', {
            'fields': ('title', ),
        }),
        ('Salary', {
            'fields':
            ('salary', 'bonus', 'bonussalary', 'stockoptions',
             'stockoptionsvalue', 'othertotal', 'allothertotal', 'extratotal',
             'stockexpense', 'restricted', 'performance', 'longtermtotal',
             'optionsexercisablevalue', 'optionsunexercisablevalue',
             'totalltequitysct', 'totalsb', 'total', 'stockaward',
             'optionaward', 'nonequityipc', 'sharesvesting', 'ylabel',
             'sayonpay'),
        }),
        ('Employees', {
            'fields': ('ceopayratio', 'medianemployeepay'),
        }),
        ('About', {
            'fields': ('footnotes', ),
        }),
        ('Internal', {
            'fields': ('notes', 'created_date', 'modified_date'),
        }),
        ('Other', {
            'classes': ('collapse', ),
            'fields':
            ('salarychange', 'bonuschange', 'longtermchange', 'nr', 'flag',
             'totalsbchange', 'totalchange', 'stockchange', 'pensionchange'),
        }),
    )


# Register other models
#admin.site.register(Company, SimpleHistoryAdmin)
#admin.site.register(Employees, SimpleHistoryAdmin)
#admin.site.register(Finances, SimpleHistoryAdmin)
admin.site.register(NonprofitFinances, SimpleHistoryAdmin)
admin.site.register(NonprofitSalary, SimpleHistoryAdmin)
#admin.site.register(OfficerSalary, SimpleHistoryAdmin)
#admin.site.register(Officer, SimpleHistoryAdmin)
