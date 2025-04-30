from django.db import models


class Tree(models.Model):
    code = models.CharField(max_length=50, unique=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    species = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.code
