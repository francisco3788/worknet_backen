from django.urls import path
from .views import RegistroCandidatoAPIView, LoginAPIView  # 👈 Importamos LoginAPIView
from .views import SolicitarRecuperacionAPIView
from .views import RestablecerContrasenaAPIView
urlpatterns = [
    path('registro-candidato/', RegistroCandidatoAPIView.as_view(), name='registro-candidato'),
    path('login/', LoginAPIView.as_view(), name='login'),  #  ruta para inicio de sesión
]

urlpatterns = [
    # ... otras rutas
    path('recuperar/', SolicitarRecuperacionAPIView.as_view(), name='recuperar'),
    path('restablecer/<uidb64>/<token>/', RestablecerContrasenaAPIView.as_view(), name='restablecer-contrasena'),
]