from rest_framework.test import APITestCase
from AppUsuarios.models import Usuario
from AppCandidatos.models import PerfilCandidato
from AppCandidatos.serializers import PerfilCandidatoSerializer
from django.core.files.uploadedfile import SimpleUploadedFile

class PerfilCandidatoSerializerTest(APITestCase):

    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            email='candidato@correo.com',
            password='password123',
            nombre_completo='Candidato Ejemplo',
            ubicacion='Bogotá'
        )
        self.perfil = PerfilCandidato.objects.create(
            usuario=self.usuario,
            descripcion='Desarrollador con experiencia',
            educacion='Ingeniero de Sistemas',
            experiencia='3 años en desarrollo web',
            habilidades='Python, Django, React',
            curriculum=SimpleUploadedFile("cv.pdf", b"archivo de prueba")
        )

    def test_serialize_modelo(self):
        serializer = PerfilCandidatoSerializer(instance=self.perfil)
        self.assertEqual(serializer.data['usuario'], self.usuario.id)
        self.assertEqual(serializer.data['descripcion'], 'Desarrollador con experiencia')
        self.assertEqual(serializer.data['educacion'], 'Ingeniero de Sistemas')
        self.assertEqual(serializer.data['experiencia'], '3 años en desarrollo web')
        self.assertEqual(serializer.data['habilidades'], 'Python, Django, React')

    def test_serializer_creacion_valida(self):
        data = {
            'usuario': self.usuario.id,
            'descripcion': 'Desarrollador backend',
            'educacion': 'Tecnólogo en programación',
            'experiencia': '2 años en backend',
            'habilidades': 'Django, DRF, PostgreSQL'
        }
        serializer = PerfilCandidatoSerializer(data=data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
