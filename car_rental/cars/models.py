from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone

def validate_year(value):
    current_year = timezone.now().year
    if value > current_year + 1:
        raise ValidationError('O ano não pode ser superior ao ano atual + 1.')

class YearField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = 'Ano'
        super().__init__(*args, **kwargs)
        self.validators.append(validate_year)


class Car(models.Model):
    	
    STATUS_CHOICES = (
        (1, 'Disponível'),
        (2, 'Manutenção'),
    )

    model = models.CharField('Modelo', max_length=100)
    plate = models.CharField('Placa', max_length=7)
    year = YearField()
    slug = models.SlugField('Atalho')
    status = models.IntegerField(
        'Situação',
        choices=STATUS_CHOICES, 
        default=1,
        blank=True
    )

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
        return reverse('cars:details', kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
        ordering = ['model']
