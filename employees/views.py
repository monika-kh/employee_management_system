from django.shortcuts import render

from rest_framework import status, mixins
from rest_framework.generics import (CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView,
                                     GenericAPIView, RetrieveUpdateDestroyAPIView)

from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin, UpdateModelMixin, \
    RetrieveModelMixin
from rest_framework.response import Response

from .models import Employees, Relationship
from .serializers import EmployeeSerializer, RelationshipSerializer

#from .signals import save_employee_salary

# Create your views here.


class EmployeeCreateView(CreateAPIView):
    #create employee
    model = Employees
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    fields = ['national_identifier']


    def create(self, request, *args, **kwargs):
        #create employee when national_identifier not exists
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            national_identifier = request.data.get('national_identifier')
            if Employees.objects.filter(national_identifier=national_identifier).exists():
                return Response({"national_identifier": "already exists"}, status=208)
            else:
                serializer.save()
                data = serializer.data

                # emp_salary = request.data.get("salary")
                # emp_deduction = request.data.get("deduction")
                # emp_earning = request.data.get("earning")
                # # breakpoint()
                # save_employee_salary.send(sender=Employees, emp_salary=emp_salary, emp_deduction=emp_deduction, emp_earning=emp_earning)



            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)


class AllEmployeeListView(ListAPIView):
    #show list of all employees
    #import paginate_by in settings
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer



class OneEmployeeRetrieveView(RetrieveAPIView):
    #show details of single employee using id

    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdateView(UpdateAPIView):
    #update method can be used for put and patch method
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
    exclude = ("national_identifier", "date_of_birth", "place_of_birth")

    def put(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            pk = request.data.get("id")
            salary = request.data.get("salary")
            deduction = request.data.get("deduction")
            earning = request.data.get("earning")
            marital_status = request.data.get("marital_status")
            position = request.data.get("position")

            update_emp = Employees.objects.get(id=pk)

            update_emp.salary = salary
            update_emp.deduction = deduction
            update_emp.earning = earning
            update_emp.marital_status = marital_status
            update_emp.position = position

            update_emp.save()

            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class EmployeeDestroyView(DestroyAPIView):
    #used to delete
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer


class RelationshipCreateView(ListModelMixin, CreateModelMixin, GenericAPIView):
    model = Relationship
    queryset = Relationship.objects.all()

    serializer_class = RelationshipSerializer

    def post(self, request, *args, **kwargs):
        serializer = RelationshipSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            employee_id = request.data.get('employee_id')
            if Relationship.objects.filter(employee_id=employee_id).exists():
                return Response({"employee_id": "already updated"}, status=208)
            else:
                serializer.save()
                data = serializer.data
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=400)
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RelationshipRetrieveUpdateDestroyView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    model = Relationship
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
        # return self.retrieve(request, *args, **kwargs)


    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        #self.perform_update(serializer)
        return Response(serializer.data)

    # def perform_update(self, serializer):
    #     serializer.save()


    def delete(self, request, *args, **kwargs):
        pk = request.data.get("id")
        relation = Relationship.objects.filter(id=pk)
        relation.delete()
        return Response({"message": "Deleted"}, status=200)



