from rest_framework import serializers
from .models import TreeEvent


class TreeEventSerializer(serializers.ModelSerializer):
    # Opcional: Exibir informações da árvore de forma mais detalhada (read-only)
    # tree_details = TreeSerializer(source='tree', read_only=True) # Exemplo de aninhamento
    # Ou apenas um campo com o código da árvore
    tree_codigo = serializers.CharField(source='tree.code', read_only=True)

    class Meta:
        model = TreeEvent
        fields = [
            'id',
            'tree',          # Ao criar/atualizar, espera-se o ID da árvore aqui.
            'tree_codigo',   # Campo read-only que adicionamos acima
            # 'tree_details', # Campo read-only aninhado (se usar o exemplo acima)
            'event_type',
            'event_date',
            'description',
        ]
        # Garante que 'tree' seja escrito (ao receber dados), mas não necessariamente lido
        # se você preferir usar 'tree_codigo' ou 'tree_details' para leitura.
        # read_only_fields = ['id', 'tree_codigo']
