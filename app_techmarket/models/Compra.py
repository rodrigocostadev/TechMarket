from django.db import models
from .Produto import Produto
from django.contrib.auth.models import User

class Compra(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name="compras_produto")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="compras_usuario")
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f" Compra do Produto: {self.produto.titulo} por {self.usuario.username} no dia {self.data_hora}")