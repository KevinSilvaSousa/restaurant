from django.contrib import admin
from pedidos.pedidosmodels import PedidoModel
@admin.register(PedidoModel)
class PedidoClienteAdmin(admin.ModelAdmin):
    def prato_cliente(self, obj):
        return ', '.join(
            [prato.nome for prato in obj.pratos.all()]
        )
    readonly_fields = ("criado_em", "atualizado_em")

    list_display = ('pedido_cliente','prato_cliente','status_pedido')