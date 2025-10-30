from django.db import models
from .Produto import Produto
from django.contrib.auth.models import User

class Movimentacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, null=True, blank=True, related_name="movimentacao_produto")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movimentacao_usuario")
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_movimentacao = models.CharField(max_length=100, )
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f" Movimentacao: {self.tipo_movimentacao} / Valor: {self.valor} / Dia {self.data_hora}")