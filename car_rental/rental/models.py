from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db import models
from car_rental.cars.models import Car


class Rental(models.Model):
    
    STATUS_CHOICES = (
        (0, 'Pendente'),
        (1, 'Aprovada'),
        (2, 'Cancelada')
    )
    status = models.IntegerField(
        'Situação',
        choices=STATUS_CHOICES, 
        default=0,
    )
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

    def __str__(self):
        return("Reserva #" + str(self.pk))
    
    # def active(self):
    #     self.status = 1
    #     self.save()
    #
    # def cancelled(self):
    #     self.status = 2
    #     self.save()

    # def is_approved(self):
    #     return self.status == 1
        

    class Meta:
        verbose_name = 'Aluguel'
        verbose_name_plural = 'Aluguéis'
        ordering = ['car','-pick_up_date','drop_off_date']
    
    def clean(self):
        self.validate_car_availability()
        self.validate_date()
        self.validate_date_overlap()

    def validate_date(self):
        current_datetime = timezone.now()
        if not self.pick_up_date < self.drop_off_date:
            raise ValidationError('Não foi possível realizar a reserva. \
                                  A data de retirada não pode ser maior que a \
                                  data de devolução.')
        
        if not self.pick_up_date > current_datetime:
            raise ValidationError('Não foi possível realizar a reserva. \
                                  A data de retirada não pode ser anterior ao \
                                  dia de hoje.')

    def validate_car_availability(self):
        if self.car.status == 2:
            raise ValidationError('Não foi possível realizar a reserva. \
                                  O veículo selecionado está em manutenção. \
                                  Por favor, selecione outro veículo') 

    def validate_date_overlap(self):

        existing_rentals = Rental.objects.filter(car=self.car).exclude(status=2)

        for rental in existing_rentals:
            if ((rental.pick_up_date <= self.pick_up_date <= rental.drop_off_date) or
                (rental.pick_up_date <= self.drop_off_date <= rental.drop_off_date) or
                (self.pick_up_date <= rental.drop_off_date <= self.drop_off_date)):
                    
                raise ValidationError('O veículo já está ocupado nessa data. \
                                      Por favor, selecione outra data')