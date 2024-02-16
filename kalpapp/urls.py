from django.urls import path,include
from rest_framework import routers
from kalpapp.views import ClientViewSet,ManagerViewSet,StaffViewSet,NumberViewSet


router = routers.DefaultRouter()
router.register(r'number',NumberViewSet)
router.register(r'manager',ManagerViewSet)
router.register(r'staff',StaffViewSet)
router.register(r'client',ClientViewSet)

urlpatterns = [
    path('',include(router.urls))
    
]
