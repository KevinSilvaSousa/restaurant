from django.contrib import admin
from django.urls import path
from cardapio.views import visualizar_cardapio

urlpatterns = [
    path('visualizar_cardapio/', visualizar_cardapio),
]