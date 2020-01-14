from django.db.models.signals import post_save
from django.dispatch import receiver
from employees.models import Employees



def save_employee_salary(sender, instance, created, **kwargs):
    if created:
        emp =  Employees.objects.all()

        id = Employees.objects.values('id')
        national_identifier = Employees.objects.values('national_identifier')


        qs = Employees.objects.filter(id=instance.id, national_identifier=instance.national_identifier)
        if qs.exists():
            employee =  Employees.objects.values('position')
            # if employee == 'CEO'
            #     salary =
            #

        #         emp_list = Employees.objects.get(all)
        #         emp_names = emp_list.eng_name
        #
        #
        # breakpoint()
        #Employees.objects.create(user=instance)


# def save_employee_salary(sender, instance, **kwargs):
#     instance.profile.save()