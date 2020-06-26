from django.db import models
from django.contrib.auth.models import User


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Table(TimeStampMixin):
    name = models.CharField(
        max_length=20,
        blank=False,
        default='',
        unique=True,
        help_text='Nombre del juego')

    words = models.TextField(
        blank=False,
        default='',
        help_text='Palabras del juego')

    hunts = models.TextField(
        blank=False,
        default='',
        help_text='Pistas del juego')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Tables'


class Game(TimeStampMixin):
    table = models.ForeignKey(Table, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    time = models.PositiveIntegerField(
        help_text='Tiempo del juego en segundos'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Games'   
