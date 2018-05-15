from tastypie.resources import ModelResource
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie.cache import SimpleCache
from tastypie import fields
from business_companies.models import Company, Employees, Finances, Officer, OfficerSalary


# Company model
class CompanyResource(ModelResource):
    #seealsoid = fields.ForeignKey(ModelResource, 'seealsoid')

    class Meta():
        queryset = Company.objects.all()
        resource_name = 'company'
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        cache = SimpleCache(cache_name='default', timeout=10)


# Employees model
class EmployeesResource(ModelResource):
    coid = fields.ForeignKey(CompanyResource, 'coid')

    class Meta:
        queryset = Employees.objects.all()
        resource_name = 'employees'
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        cache = SimpleCache(cache_name='default', timeout=10)


# Finances model
class FinancesResource(ModelResource):
    coid = fields.ForeignKey(CompanyResource, 'coid')

    class Meta:
        queryset = Finances.objects.all()
        resource_name = 'finances'
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        cache = SimpleCache(cache_name='default', timeout=10)


# Officer model
class OfficerResource(ModelResource):
    coid = fields.ForeignKey(CompanyResource, 'coid')

    # calculated_total = fields.DecimalField(
    #     attribute='calculated_total', readonly=True, blank=True)

    class Meta:
        queryset = Officer.objects.all()
        resource_name = 'officer'
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        cache = SimpleCache(cache_name='default', timeout=10)


# OfficerSalary model
class OfficerSalaryResource(ModelResource):
    officerid = fields.ForeignKey(OfficerResource, 'officerid')
    calculated_total_value = fields.FloatField(
        attribute='calculated_total_value', readonly=True, blank=True)

    class Meta:
        queryset = OfficerSalary.objects.all()
        resource_name = 'officer_salary'
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        cache = SimpleCache(cache_name='default', timeout=10)
