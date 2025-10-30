from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    imagem = models.FileField(upload_to='media/imagens_perfil/', blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.username} (Saldo: R$ {self.saldo})"