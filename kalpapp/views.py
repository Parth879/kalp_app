from django.shortcuts import render
from rest_framework import viewsets
from kalpapp.models import Number,Manager,Staff,Client
from kalpapp.serializers import ClientSerializer,ManagerSerializer,NumberSerializer,StaffSerializer
from rest_framework.response import Response



class NumberViewSet(viewsets.ModelViewSet):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer