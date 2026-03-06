from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ("flooding", "Flooding"),
    ("water-quality", "Water Quality"),
    ("drainage", "Drainage"),
    ("urban-runoff", "Urban Runoff"),
    ("infrastructure", "Infrastructure Damage"),
    ("other", "Other Issues"),
]

STATUS_CHOICES = [
    ("pending", "Pending"),
    ("in_progress", "In Progress"),
    ("resolved", "Resolved"),
]

class WaterIssueReport(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports")

    title = models.CharField(max_length=255)
    description = models.TextField()

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    image = models.ImageField(upload_to='reports/')

    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title