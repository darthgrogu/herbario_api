from django.db import models


class Tree(models.Model):
    accession = models.CharField(max_length=50, unique=True)
    familyname = models.CharField(max_length=100, blank=True, null=True)
    vernacularname = models.CharField(max_length=100, blank=True, null=True)
    calcfullname = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.code
