from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Company, Employees, Finances, NonprofitFinances, NonprofitSalary, OfficerSalary, Officer

# Referenence
# https://docs.djangoproject.com/en/2.0/ref/contrib/admin/

# Customize inline admin interfaces
# https://docs.djangoproject.com/en/2.0/ref/contrib/admin/#inlinemodeladmin-objects
class EmployeesInline(admin.TabularInline):
    model = Employees
    extra = 0
    show_change_link = True
    fields = ('added', 'publishyear', 'parttime', 'fulltime', 'union', 'total', 'minnesota')

# Customize main admin interface for Company
@admin.register(Company)
class CompanyAdmin(SimpleHistoryAdmin):
    #date_hierarchy = 'modified_date'
    list_display = ('coid', 'name', 'stocksymbol', 'category', 'companytype', 'shortdesc')
    list_filter = ('category', 'companytype')
    search_fields = ['coid', 'name', 'stocksymbol']
    autocomplete_fields = ['seealsoid']
    inlines = [EmployeesInline]

# Register other models
#admin.site.register(Company, SimpleHistoryAdmin)
admin.site.register(Employees, SimpleHistoryAdmin)
admin.site.register(Finances, SimpleHistoryAdmin)
admin.site.register(NonprofitFinances, SimpleHistoryAdmin)
admin.site.register(NonprofitSalary, SimpleHistoryAdmin)
admin.site.register(OfficerSalary, SimpleHistoryAdmin)
admin.site.register(Officer, SimpleHistoryAdmin)
