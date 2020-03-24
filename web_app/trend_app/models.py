from django.db import models
from django.contrib.postgres.fields import JSONField

class Description(models.Model):
    graph_name = models.CharField(max_length=255)
    x_axis_name = models.CharField(max_length=255)
    y_axis_name = models.CharField(max_length=255)

class Trend(models.Model):
    json = JSONField()
    desc = models.ForeignKey(
        Description,
        on_delete=models.CASCADE,
        related_name='trend'
    )