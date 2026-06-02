from django.contrib import admin
from pedidos.models.itempedidomodels import ItemPedidoModel
from pedidos.models.pedidosmodels import PedidoModel


admin.site.register(ItemPedidoModel)
#admin.site.register(PedidoModel )

@admin.register(PedidoModel)
class PedidoClienteAdmin(admin.ModelAdmin):
    readonly_fields = ("criado_em", "atualizado_em")

    list_display = ('prato_cliente','tamanho_lanche','criado_em', 'atualizado_em', 'status_pedido')