from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator


def validate_year(value):
    current_year = timezone.now().year
    if value > current_year + 1:
        raise ValidationError('O ano não pode ser superior ao ano atual + 1.')
    if value <= 0:
        raise ValidationError('O ano não pode ser negativo (inferior a 0).')
    if value < current_year - 100:
        raise ValidationError('O ano não pode ser inferior ao ano atual - 100.')

class YearField(models.IntegerField):
    def __init__(self, *args, **kwargs):
        kwargs['verbose_name'] = 'Ano'
        super().__init__(*args, **kwargs)
        self.validators.append(validate_year)


class Car(models.Model):

    plate_regex = RegexValidator(
        regex=r'^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$',
        message="A placa do veículo precisa estar nos formatos: \
        'AAA0A00' ou 'AAA0000'"
    )
    	
    STATUS_CHOICES = (
        (1, 'Disponível'),
        (2, 'Manutenção'),
    )

    model = models.CharField('Modelo', max_length=100)
    plate = models.CharField(
        'Placa', 
        unique=True,
        max_length=7,
        validators=[plate_regex]
    )
    year = YearField()
    # slug deixou de ser usado e foi substituido pela pk 
    slug = models.SlugField('Atalho')
    status = models.IntegerField(
        'Situação',
        choices=STATUS_CHOICES, 
        default=1,
    )
    photo = models.ImageField(
        upload_to='cars/images/',
        verbose_name='Imagem',
        null=True,
        blank=True
    )

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.model
    
    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
        ordering = ['model']
