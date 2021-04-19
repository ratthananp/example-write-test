from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from main.apps.departments.models import Department, Company
from main.apps.departments.serializers import DepartmentSerializer, CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CompanySerializer
    queryset = Company.objects.order_by('id')


class DepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = DepartmentSerializer
    queryset = Department.objects.order_by('id')
