from django.db import models

class Produto(models.Model):
    titulo = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)    
    descricao = models.TextField()
    imagem = models.FileField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return (f"Produto: {self.titulo}, Preço: {self.preco}")

