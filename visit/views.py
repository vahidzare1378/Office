from django.db.models import query
from rest_framework import viewsets, permissions
from visit import serializers
from visit import models

class DoctorProfileView(viewsets.ModelViewSet):
    queryset = models.DoctorProfile.objects.all()
    serializer_class = serializers.DoctorProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class PatientProfileView(viewsets.ModelViewSet):
    queryset = models.PatientProfile.objects.all()
    serializer_class = serializers.PatientProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)
        
class VisitView(viewsets.ModelViewSet):
    queryset = models.Visit.objects.all()
    serializer_class = serializers.VisitSerializer

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)