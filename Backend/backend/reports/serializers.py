from rest_framework import serializers
from .models import WaterIssueReport

class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = WaterIssueReport
        fields = '__all__'
        read_only_fields = ['user']