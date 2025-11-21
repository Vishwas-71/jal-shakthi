from django.db import models

CATEGORY_CHOICES = [
    ("flooding", "Flooding"),
    ("water-quality", "Water Quality"),
    ("drainage", "Drainage"),
    ("urban-runoff", "Urban Runoff"),
    ("infrastructure", "Infrastructure Damage"),
    ("other", "Other Issues"),
]

class WaterIssueReport(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='reports/')
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class TestModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Report(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.title
