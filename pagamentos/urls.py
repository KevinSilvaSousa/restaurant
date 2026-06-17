from django.urls import path
from .views import criar_pagamento

urlpatterns = [
    path('criar_pagamento/', criar_pagamento),
    
]
