from rest_framework import serializers
from .models import WaterIssueReport
from .models import Report
class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterIssueReport
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
