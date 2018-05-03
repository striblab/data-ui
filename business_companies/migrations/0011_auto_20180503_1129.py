# Generated by Django 2.0.4 on 2018-05-03 16:29

from django.db import migrations

# Create group to manage data
def create_business_companies_group(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Permission = apps.get_model("auth", "Permission")

    group, created = Group.objects.get_or_create(name='Business Companies')
    if created:
        permissions = Permission.objects.filter(
            codename__in=[
                'add_company', 'add_historicalcompany',
                'change_company',
                'delete_company',

                'add_employees', 'add_historicalemployees',
                'change_employees',
                'delete_employees',

                'add_finances', 'add_historicalfinances',
                'change_finances',
                'delete_finances',

                'add_nonprofitfinances', 'add_historicalnonprofitfinances',
                'change_nonprofitfinances',
                'delete_nonprofitfinances',

                'add_nonprofitsalary', 'add_historicalnonprofitsalary',
                'change_nonprofitsalary',
                'delete_nonprofitsalary',

                'add_salary', 'add_historicalsalary',
                'change_salary',
                'delete_salary',

                'add_officer', 'add_historicalofficer',
                'change_officer',
                'delete_officer'
            ]
        )
        group.permissions.set(permissions)
        group.save()


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
        ('business_companies', '0010_auto_20180503_1055'),
    ]

    operations = [
        migrations.RunPython(create_business_companies_group),
    ]
