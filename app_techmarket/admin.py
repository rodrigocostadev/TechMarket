from django.contrib import admin
from .models.Compra import Compra 
from .models.Produto import Produto

admin.site.register(Compra)
admin.site.register(Produto)
