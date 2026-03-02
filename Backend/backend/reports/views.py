from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import WaterIssueReport
from .serializers import ReportSerializer


class ReportViewSet(ModelViewSet):
    queryset = WaterIssueReport.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)