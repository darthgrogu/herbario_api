from rest_framework import serializers
from bosque_trees.models import Tree


class TreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tree
        fields = ['id', 'accession', 'familyname', 'calcfullname', 'vernacularname', 'latitude', 'longitude']
