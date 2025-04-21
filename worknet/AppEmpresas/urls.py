from django.urls import path
from .views import RegistroEmpresaAPIView

urlpatterns = [
    path('registro-empresa/', RegistroEmpresaAPIView.as_view(), name='registro-empresa'),
]
