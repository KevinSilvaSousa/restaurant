from django.contrib import admin
from pedidos.models.pedidosmodels import PedidoModel
from .models.item_pedido_models import ItemPedido

admin.site.register(ItemPedido)
@admin.register(PedidoModel)
class PedidoClienteAdmin(admin.ModelAdmin):
    def prato_cliente(self, obj):
        return ', '.join( str(item.prato)
             for item in obj.itens.all()
    )
    readonly_fields = ("criado_em", "atualizado_em")

    list_display = ('pedido_cliente','prato_cliente','status_pedido')