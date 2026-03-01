from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend

from .models import WaterIssueReport
from .serializers import ReportSerializer


class ReportViewSet(viewsets.ModelViewSet):

    queryset = WaterIssueReport.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'category']
    search_fields = ['title', 'description', 'address']
    ordering_fields = ['created_at']

    def get_queryset(self):
        if self.request.user.is_staff:
            return WaterIssueReport.objects.all()
        return WaterIssueReport.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        if not self.request.user.is_staff:
            if 'status' in serializer.validated_data:
                raise PermissionDenied("You are not allowed to change status.")
        serializer.save()