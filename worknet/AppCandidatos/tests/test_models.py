from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from AppUsuarios.models import Usuario
from AppCandidatos.models import PerfilCandidato

class PerfilCandidatoModelTest(TestCase):

    def setUp(self):
        self.usuario = Usuario.objects.create_user(
            email='candidato@correo.com',
            password='testpass123',
            nombre_completo='Candidato Ejemplo',
            ubicacion='Bogotá'
        )

        self.perfil = PerfilCandidato.objects.create(
            usuario=self.usuario,
            descripcion='Soy un desarrollador entusiasta.',
            educacion='Ingeniería de Sistemas - Universidad X',
            experiencia='2 años en desarrollo web',
            habilidades='Python, Django, React',
            curriculum=SimpleUploadedFile("cv.pdf", b"contenido de prueba")
        )

    def test_str_metodo(self):
        self.assertEqual(str(self.perfil), f"Perfil de {self.usuario.email}")

    def test_campos_perfil(self):
        self.assertEqual(self.perfil.descripcion, 'Soy un desarrollador entusiasta.')
        self.assertEqual(self.perfil.educacion, 'Ingeniería de Sistemas - Universidad X')
        self.assertEqual(self.perfil.experiencia, '2 años en desarrollo web')
        self.assertEqual(self.perfil.habilidades, 'Python, Django, React')
        self.assertTrue(self.perfil.curriculum.name.endswith('cv.pdf'))
