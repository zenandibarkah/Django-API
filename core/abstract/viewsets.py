from rest_framework import viewsets
from rest_framework import filters

class AbstractViewSets(viewsets.ModelViewSet):
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['updated','created'] # fields that can be used as ordering parameters
    ordering = ['-updated']