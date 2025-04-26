from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.urls import reverse
from AppUsuarios.models import Usuario
from AppCandidatos.models import PerfilCandidato

class CrearPerfilCandidatoViewTest(APITestCase):

    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            email='candidato@correo.com',
            password='testpass123',
            nombre_completo='Candidato Ejemplo',
            ubicacion='Cartagena'
        )
        self.token = Token.objects.create(user=self.usuario)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_crear_perfil_candidato_exitoso(self):
        url = reverse('crear-perfil-candidato')
        data = {
            "descripcion": "Candidato con experiencia en desarrollo web",
            "educacion": "Ingeniería de Sistemas - Universidad XYZ",
            "experiencia": "2 años como desarrollador backend",
            "habilidades": "Python, Django, SQL",
            "foto": None,
            "curriculum": None
        }
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["mensaje"], "Perfil de candidato creado exitosamente")
        self.assertTrue(PerfilCandidato.objects.filter(usuario=self.usuario).exists())

    def test_crear_perfil_candidato_invalido(self):
        url = reverse('crear-perfil-candidato')
        data = {
            "descripcion": "",
            "educacion": "",
            "experiencia": "",
            "habilidades": "",
        }
        response = self.client.post(url, data, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
