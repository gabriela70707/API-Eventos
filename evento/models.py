from django.db import models

# Create your models here.
class Event(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=300)
    data = models.DateField()
    hora = models.TimeField()
    local = models.CharField(max_length=200, blank=True)
    categorias = [('Musica','Musica'), ('Palestra', 'Palestra'), ('Workshop', 'Workshop')]
    categoria = models.CharField(max_length=200, choices=categorias)


    def __str__(self):
        return self.nome