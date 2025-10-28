from django.db import models

class Produto(models.Model):
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return (f"Produto: {self.titulo}, Preço: {self.preco}")

