from rest_framework import viewsets
from .models import WaterIssueReport
from .serializers import ReportSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = WaterIssueReport.objects.all()
    serializer_class = ReportSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Report
from .serializers import ReportSerializer

@api_view(['GET'])
def get_all_reports(request):
    reports = Report.objects.all()
    serializer = ReportSerializer(reports, many=True)
    return Response(serializer.data)
