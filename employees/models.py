# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from django.db import models


# Create your models here.

class Employees(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    Position_CHOICES = [
        ('Employee', 'Employee'),
        ('Manager', 'Manager'),
        ('CEO', 'CEO'),
    ]
    MARITAL_STATUS_CHOICES = [
        ('Single', 'Single'),
        ('Married', 'Married'),
    ]
    first_name = models.CharField(max_length=255)
    # middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    # full_name = models.CharField(max_length=500)
    national_identifier = models.BigIntegerField(unique=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=25)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=255)
    position = models.CharField(choices=Position_CHOICES, max_length=25)
    # job = models.CharField(max_length=255, null=True)
    # country = models.CharField(max_length=255)
    # nationality = models.CharField(max_length=255)
    marital_status = models.CharField(choices=MARITAL_STATUS_CHOICES, max_length=25)
    salary = models.PositiveIntegerField()
    deduction = models.PositiveIntegerField(default=0, null=True)
    earning = models.PositiveIntegerField(default=0, null=True)

    # deduction_description = models.TextField(null=True)
    # earning_description = models.TextField(null=True)
    # activated = models.BooleanField(default=True)
    # freeze = models.BooleanField(default=False)
    # added = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


class Relationship(models.Model):
    RELATIONSHIP_TYPE_CHOICES = [
        ('wife', 'Wife'),
        ('child', 'Child'),
        ('husband', 'Husband'),
    ]
    employee_id = models.ForeignKey(Employees, on_delete=models.CASCADE, related_name="employee")
    relationship_type = models.CharField(choices=RELATIONSHIP_TYPE_CHOICES, max_length=25)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.relationship_type


# def save_employee_salary(sender, instance, created, **kwargs):
#     if created:
#         qs = Employees.objects.filter(id=instance.id, national_identifier=instance.national_identifier)
#         if qs.exists() and qs.count() == 1:
#             employee = qs.first()
#             breakpoint()
#             position = employee.position
#             if position == 'Employee':
#                 deduction = (employee.salary * 7.5) / 100
#                 employee.deduction = deduction
#                 employee.save()
#             if position == 'Manager':
#                 deduction = (employee.salary * 12) / 100
#                 employee.deduction = deduction
#                 employee.save()
#             if position == 'CEO':
#                 deduction = (employee.salary * 15) / 100
#                 employee.deduction = deduction
#                 employee.save()
#
#
# post_save.connect(save_employee_salary, sender=Employees)