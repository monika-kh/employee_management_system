from . models import *
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"


class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = "__all__"

    def to_representation(self, instance):                                           #represent employee's first_name, but for post method use employee id
        rep = super(RelationshipSerializer, self).to_representation(instance)
        rep['employee_id'] = instance.employee_id.first_name
        return rep