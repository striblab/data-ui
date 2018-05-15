from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.authorization import DjangoAuthorization
from tastypie.authentication import ApiKeyAuthentication
from business_companies.models import Company, Employees


# Abstract class for all models
class BaseResource(ModelResource):
    class Meta:
        abstract = True
        allowed_methods = ['get']
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()


# Company model
class CompanyResource(BaseResource):
    #seealsoid = fields.ForeignKey(ModelResource, 'seealsoid')

    class Meta:
        queryset = Company.objects.all()
        resource_name = 'company'
        #excludes = ['field']


# Employees model
class EmployeesResource(BaseResource):
    coid = fields.ForeignKey(CompanyResource, 'coid')

    class Meta:
        queryset = Employees.objects.all()
        resource_name = 'employees'
