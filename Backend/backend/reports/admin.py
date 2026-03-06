from django.contrib import admin
from .models import WaterIssueReport


@admin.register(WaterIssueReport)
class WaterIssueReportAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "status",
        "user",
        "created_at"
    )

    list_filter = (
        "status",
        "category"
    )

    search_fields = (
        "title",
        "description",
        "address"
    )