from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
from .models import Company, Employees, Finances, NonprofitFinances, NonprofitSalary, OfficerSalary, Officer

admin.site.register(Company, SimpleHistoryAdmin)
admin.site.register(Employees, SimpleHistoryAdmin)
admin.site.register(Finances, SimpleHistoryAdmin)
admin.site.register(NonprofitFinances, SimpleHistoryAdmin)
admin.site.register(NonprofitSalary, SimpleHistoryAdmin)
admin.site.register(OfficerSalary, SimpleHistoryAdmin)
admin.site.register(Officer, SimpleHistoryAdmin)
