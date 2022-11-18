from django.contrib.auth import get_user_model
from django.db import models

# - Relacionamento Um para Um (OneToOneField)
# Cada carro só pode ter relacionamento com 1 chassi
# Cada chassi também só pode estar relacionado a um carro.

# - Relacionamento Um para Muitos (ForeignKey - One to Many)
# Cada carro tem sua montadora
# Cada montadora tem diversos carros

# - Relacionamento Muitos para Muitos (Many to Many)
# Cada carro poderá ter vários motoristas (motoristas=user)
# Cada motorista poderá ter vários carros

class Chassi(models.Model):
    numero = models.CharField('Chassi', max_length=16, help_text='Máximo 16 caracteres')
    
    class Meta:
        verbose_name = 'Chassi'
        verbose_name_plural = 'Chassis'
    
    def __str__(self):
        return self.numero


class Montadora(models.Model):
    nome = models.CharField('Nome', max_length=50)
    
    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'
    
    def __str__(self):
        return self.nome
    

def set_default_montadora():
    return Montadora.objects.get_or_create(nome='Padrão')[0]  #[0] pra sempre trazer o objeto


class Carro(models.Model):
    chassi = models.OneToOneField(Chassi, on_delete=models.CASCADE)
    montadora = models.ForeignKey(Montadora, on_delete=models.SET(set_default_montadora))
    motoristas = models.ManyToManyField(get_user_model())
    modelo = models.CharField('Modelo', max_length=30, help_text='Máximo 30 caracteres')
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2) # pode ser até 99999999,99
    
    class Meta:
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'
    
    def __str__(self):
        return f'{self.montadora} {self.modelo}'