from django.db import models
from django.contrib.auth.models import User

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil_usuario")
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    imagem = models.FileField(upload_to='media/imagens_perfil/', blank=True, null=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    data_nascimento = models.CharField(max_length=10, blank=True, null=True)
    numero_telefone = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.username} (Saldo: R$ {self.saldo})"