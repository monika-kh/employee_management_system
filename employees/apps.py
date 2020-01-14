# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.db.models.signals import post_save

from .models import Employees
from . signals import employee_salary, save_employee_salary

class EmployeesConfig(AppConfig):
    name = 'employees'



def ready(self):
    post_save.connect(employee_salary, sender=Employees)
    post_save.connect(save_employee_salary, sender=Employees)