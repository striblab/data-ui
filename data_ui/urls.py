"""data_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
# API resources
from tastypie.api import Api
from business_companies.api import CompanyResource, EmployeesResource, FinancesResource, NonprofitFinancesResource, OfficerResource, OfficerSalaryResource, CompanyDetailsResource
v1_api = Api(api_name='v01')
v1_api.register(CompanyResource())
v1_api.register(EmployeesResource())
v1_api.register(FinancesResource())
v1_api.register(NonprofitFinancesResource())
v1_api.register(OfficerResource())
v1_api.register(OfficerSalaryResource())
v1_api.register(CompanyDetailsResource())

# Update some variables in the admin
admin.site.site_header = 'Data UI'
admin.site.site_title = 'Star Tribune Data UI'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='admin/')),
    path('api/', include(v1_api.urls)),
]

# Debug bar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__', include(debug_toolbar.urls)),
    ] + urlpatterns
