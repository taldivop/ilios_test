from django.db import models
from car_rental.cars.models import Car


class Rental(models.Model):
    
    car = models.ForeignKey(
        Car, verbose_name='Carro',
        on_delete=models.CASCADE,
        related_name='rentals'
    )
    pick_up_date = models.DateTimeField('Data de Retirada')
    drop_off_date = models.DateTimeField('Data de Entrega')
    observations = models.TextField('Observações', max_length=100, blank=True)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Aluguel'
        verbose_name_plural = 'Aluguéis'
        ordering = ['car','-pick_up_date','drop_off_date']
    