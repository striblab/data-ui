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
    fields = ('added', 'publishyear', 'parttime', 'fulltime', 'union', 'total', 'minnesota')

class OfficerInline(admin.TabularInline):
    model = Officer
    extra = 0
    show_change_link = True
    fields = ('dropped', 'title', 'first', 'last')

class FinancesInline(admin.TabularInline):
    model = Finances
    extra = 0
    show_change_link = True
    fields = ('publishyear', 'revenue', 'ati', 'netincome', 'marketcap', 'totalassets')

# Customize main admin interface for Company
@admin.register(Company)
class CompanyAdmin(SimpleHistoryAdmin):
    #date_hierarchy = 'modified_date'
    list_display = ('coid', 'name', 'stocksymbol', 'category', 'companytype', 'shortdesc')
    list_filter = ('category', 'companytype')
    search_fields = ['coid', 'name', 'stocksymbol']
    autocomplete_fields = ['seealsoid']
    inlines = [EmployeesInline, OfficerInline, FinancesInline]
    fieldsets = (
        (None, {
            'fields': ('coid', 'added', 'name', 'alpha', 'irsno', 'stocksymbol', 'exchange')
        }),
        ('Grouping', {
            #'classes': ('collapse',),
            'fields': ('companytype', 'category'),
        }),
        ('About', {
            'fields': ('description', 'companyhistory', 'shortdesc', 'founded', 'inc', 'incst',
            'footnotes', 'annualmeet', 'fymonth', 'class_field'),
        }),
        ('References', {
            'fields': ('seealso', 'seealsoid'),
        }),
        ('Address', {
            'fields': ('address1', 'address2', 'city', 'state', 'zip', 'phone', 'fax', 'www'),
        }),
        ('Main contact', {
            'fields': ('contact', 'contactphone', 'contactemail'),
        }),
        ('Internal', {
            'fields': ('notes', 'enteredby'),
        }),
    )

@admin.register(Employees)
class EmployeesAdmin(SimpleHistoryAdmin):
    list_display = ('coid', 'publishyear', 'added', 'total')
    search_fields = ['coid__name', 'publishyear']
    autocomplete_fields = ['coid']
    fieldsets = (
        (None, {
            'fields': ('coid', 'added', 'publishyear')
        }),
        ('Employees', {
            'fields': ('total', 'parttime', 'fulltime', 'union', 'minnesota'),
        }),
        ('About', {
            'fields': ('footnotes', ),
        }),
        ('Internal', {
            'fields': ('notes', ),
        }),
    )

# Register other models
#admin.site.register(Company, SimpleHistoryAdmin)
#admin.site.register(Employees, SimpleHistoryAdmin)
admin.site.register(Finances, SimpleHistoryAdmin)
admin.site.register(NonprofitFinances, SimpleHistoryAdmin)
admin.site.register(NonprofitSalary, SimpleHistoryAdmin)
admin.site.register(OfficerSalary, SimpleHistoryAdmin)
admin.site.register(Officer, SimpleHistoryAdmin)
