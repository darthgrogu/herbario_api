from django.db import models
from bosque_trees.models import Tree


class TreeEvent(models.Model):
    tree = models.ForeignKey(
        Tree,
        on_delete=models.CASCADE,
        related_name='events',
        help_text="A árvore à qual este evento está associado."
    )

    EVENT_TYPES = [
        ('PODA', 'Poda'),
        ('DOENCA', 'Doença Identificada'),
        ('TRATAMENTO', 'Tratamento Aplicado'),
        ('ADUBACAO', 'Adubação'),
        ('MONITORAMENTO', 'Monitoramento Geral'),
        ('FLORACAO', 'Floração'),
        ('FRUTIFICACAO', 'Frutificação'),

    ]
    event_type = models.CharField(
        max_length=50,
        choices=EVENT_TYPES,
        help_text="Tipo de evento ocorrido."
    )
    event_date = models.DateTimeField(
        # auto_now_add=True, # Define automaticamente na criação (não editável)
        # default=timezone.now, # Define padrão como agora, mas permite editar
        null=True, blank=True,
        help_text="Data e hora em que o evento ocorreu ou foi registrado."
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Descrição detalhada do evento."
    )

    def __str__(self):
        type_display = self.get_event_type_display() if self.event_type else 'N/A'
        tree_display = str(self.tree) if self.tree else 'Árvore Desconhecida'
        date_display = self.event_date.strftime("%Y-%m-%d %H:%M") if self.event_date else 'Data Desconhecida'
        return f"{type_display} em {tree_display} - {date_display}"

    class Meta:
        verbose_name = "Evento da Árvore"
        verbose_name_plural = "Eventos das Árvores"
        ordering = ['-event_date', 'id']
