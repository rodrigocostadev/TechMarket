from django.contrib import admin
from .models.Compra import Compra 
from .models.Produto import Produto
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import PerfilUsuario
from .models import Movimentacao

class PerfilUsuarioInline(admin.StackedInline):
    model = PerfilUsuario
    can_delete = False
    verbose_name_plural = 'Perfil do Usuário'

class UserAdmin(BaseUserAdmin):
    inlines = (PerfilUsuarioInline,)

# Cancela o admin padrão do User
admin.site.unregister(User)

# Registra o novo admin com o inline
admin.site.register(User, UserAdmin)

admin.site.register(Compra)
admin.site.register(Produto)
admin.site.register(Movimentacao)
