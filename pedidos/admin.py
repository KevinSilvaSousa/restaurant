from django.contrib import admin
from pedidos.models.itempedidomodels import ItemPedidoModel
from pedidos.models.pedidosmodels import PedidoModel


admin.site.register(ItemPedidoModel)
admin.site.register(PedidoModel)