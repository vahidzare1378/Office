from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from visit import views

router = DefaultRouter()
router.register('doctor', views.DoctorProfileView)
router.register('patient', views.PatientProfileView)
router.register('visit', views.VisitView)

urlpatterns = [
    path('', include(router.urls))
]