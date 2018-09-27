from django.conf.urls import url, include
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie.cache import SimpleCache
from tastypie.utils import trailing_slash
from tastypie import fields
from business_companies.models import Company, Employees, Finances, NonprofitFinances, Officer, OfficerSalary, NonprofitSalary


# Company model
class CompanyResource(ModelResource):
    seealsoid = fields.ForeignKey(
        ModelResource, 'seealsoid', blank=True, null=True)

    class Meta():
        queryset = Company.objects.all()
        resource_name = 'company'
        filtering = {
            'coid': ALL,
            'name': ALL,
            'companytype': ALL,
            'category': ALL,
            'dropped': ALL
        }
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        cache = SimpleCache(cache_name='default', timeout=10)


# Employees model
class EmployeesResource(ModelResource):
    #coid = fields.ForeignKey(CompanyResource, 'coid', full=True)
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


# NonprofitFinances model
class NonprofitFinancesResource(ModelResource):
    coid = fields.ForeignKey(CompanyResource, 'coid')

    class Meta:
        queryset = NonprofitFinances.objects.all()
        resource_name = 'nonprofit_finances'
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        cache = SimpleCache(cache_name='default', timeout=10)


# Officer model
class OfficerResource(ModelResource):
    coid = fields.ForeignKey(CompanyResource, 'coid')
    salaries = fields.ToManyField(
        'business_companies.api.OfficerSalaryResource',
        # Make sure there is a related_name on the foreign key in the model
        'salary_officer',
        related_name='salary_officer',
        null=True,
        full=True)

    nonprofit_salaries = fields.ToManyField(
        'business_companies.api.NonprofitSalaryResource',
        # Make sure there is a related_name on the foreign key in the model
        'nonprofit_officer',
        related_name='nonprofit_officer',
        null=True,
        full=True)

    class Meta:
        queryset = Officer.objects.all()
        resource_name = 'officer'
        allowed_methods = ['get']
        filtering = {
            'first': ALL,
            'last': ALL,
            'title': ALL,
            'coid': ALL_WITH_RELATIONS,
        }
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        cache = SimpleCache(cache_name='default', timeout=10)


# Officer simple model, specificlly without salaries, so that salaries
# can pull officers without recursion
class OfficerSimpleResource(ModelResource):
    coid = fields.ForeignKey(CompanyResource, 'coid', full=True)

    class Meta:
        queryset = Officer.objects.all()
        resource_name = 'officer'
        allowed_methods = ['get']
        filtering = {
            'first': ALL,
            'last': ALL,
            'title': ALL,
            'coid': ALL_WITH_RELATIONS,
        }
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        cache = SimpleCache(cache_name='default', timeout=10)


# OfficerSalary model
class OfficerSalaryResource(ModelResource):
    officerid = fields.ForeignKey(
        OfficerSimpleResource, 'officerid', full=True)
    calculated_total_value = fields.FloatField(
        attribute='calculated_total_value', readonly=True, blank=True)

    class Meta:
        queryset = OfficerSalary.objects.all()
        resource_name = 'officer_salary'
        allowed_methods = ['get']
        filtering = {
            'publishyear': ALL,
            'title': ALL,
            'officerid': ALL_WITH_RELATIONS,
            'officerid__coid': ALL_WITH_RELATIONS,
        }
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        cache = SimpleCache(cache_name='default', timeout=10)


# NonprofitSalary model
class NonprofitSalaryResource(ModelResource):
    officerid = fields.ForeignKey(
        OfficerSimpleResource, 'officerid', full=True)

    class Meta:
        queryset = NonprofitSalary.objects.all()
        resource_name = 'nonprofit_salary'
        allowed_methods = ['get']
        filtering = {
            'publishyear': ALL,
            'title': ALL,
            'officerid': ALL_WITH_RELATIONS,
            'officerid__coid': ALL_WITH_RELATIONS,
        }
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        cache = SimpleCache(cache_name='default', timeout=10)


# Company details model
class CompanyDetailsResource(ModelResource):
    seealsoid = fields.ForeignKey(
        ModelResource, 'seealsoid', blank=True, null=True)
    officers = fields.ToManyField(
        'business_companies.api.OfficerResource',
        'officer_company',
        related_name='officer_company',
        null=True,
        full=True)
    finances = fields.ToManyField(
        'business_companies.api.FinancesResource',
        'finances_company',
        related_name='finances_company',
        null=True,
        full=True)
    nonprofit_finances = fields.ToManyField(
        'business_companies.api.NonprofitFinancesResource',
        'nonprofit_finances_company',
        related_name='nonprofit_finances_company',
        null=True,
        full=True)
    employees = fields.ToManyField(
        'business_companies.api.EmployeesResource',
        'employees_company',
        related_name='employees_company',
        null=True,
        full=True)

    # Add custom filters, specifically to get a specific set
    # of companies.
    def build_filters(self, filters=None):
        if filters is None:
            filters = {}
        orm_filters = super(CompanyDetailsResource,
                            self).build_filters(filters)

        if ('finance_publishyear' in filters):
            finance_publishyear = filters['finance_publishyear']
            finances = Finances.objects.filter(publishyear=finance_publishyear)
            coids = [f.coid.coid for f in finances]
            orm_filters.update({'coid__in': coids})

        if ('nonprofit_finance_publishyear' in filters):
            nonprofit_finance_publishyear = filters[
                'nonprofit_finance_publishyear']
            finances = NonprofitFinances.objects.filter(
                publishyear=nonprofit_finance_publishyear)
            coids = [f.coid.coid for f in finances]
            orm_filters.update({'coid__in': coids})

        return orm_filters

    class Meta():
        queryset = Company.objects.all()
        resource_name = 'company_details'
        filtering = {
            'coid': ALL,
            'name': ALL,
            'companytype': ALL,
            'category': ALL,
            'dropped': ALL
        }
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
        cache = SimpleCache(cache_name='default', timeout=100)
