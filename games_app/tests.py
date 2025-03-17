from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from games_app import models

class DeveloperTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(username='admin',email='admin@example.com',password='adminpassword')
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        # Crear un desarrollador de prueba
        self.developer = models.Developer.objects.create(
            name="Ubisoft",
            description="This is a description",
            country="USA",
            web_site="https://www.ubisoft.com"
        )
        #self.stream = models.StreamPlatform.objects.create(name="Netflix", about="#1 Platform", website="https://www.netflix.com")
    def test_developer_create(self):
        data = {
            "name":"Ubisoft",
            "description": "This is a description",
            "country": "USA",
            "web_site": "www.ubisoft.com"
        }
        response = self.client.post(reverse('developer-list'),data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    def test_developer_create_invalid_data(self):
        """
        Prueba la creación de un desarrollador con datos inválidos.
        """
        data = {
            "name": "",  # Nombre vacío (inválido)
            "description": "This is a description",
            "country": "USA",
            "web_site": "https://www.ubisoft.com"
        }
        response = self.client.post(reverse('developer-list'), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    def test_developer_list(self):
        """
        Prueba la obtención de la lista de desarrolladores.
        """
        # Crear algunos desarrolladores de prueba
        models.Developer.objects.create(
            name="Ubisoft",
            description="This is a description",
            country="USA",
            web_site="https://www.ubisoft.com"
        )
        models.Developer.objects.create(
            name="EA Games",
            description="Another description",
            country="Canada",
            web_site="https://www.ea.com"
        )

        response = self.client.get(reverse('developer-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # Verificar que se devuelvan 2 desarrolladores
    def test_developer_create_unauthenticated(self):
        """
        Prueba la creación de un desarrollador sin autenticación.
        """
        self.client.credentials()  # Eliminar la autenticación
        data = {
            "name": "Ubisoft",
            "description": "This is a description",
            "country": "USA",
            "web_site": "https://www.ubisoft.com"
        }
        response = self.client.post(reverse('developer-list'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    def test_developer_update(self):
        """
        Prueba la actualización de un desarrollador existente.
        """
        data = {
            "name": "Ubisoft Updated",
            "description": "Updated description",
            "country": "France",
            "web_site": "https://www.ubisoft.fr"
        }
        response = self.client.put(
            reverse('developer-detail', kwargs={'pk': self.developer.pk}),
            data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.developer.refresh_from_db()
        self.assertEqual(self.developer.name, "Ubisoft Updated")
        self.assertEqual(self.developer.country, "France")
    def test_developer_delete(self):
        """
        Prueba la eliminación de un desarrollador existente.
        """
        response = self.client.delete(
            reverse('developer-detail', kwargs={'pk': self.developer.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.Developer.objects.count(), 0)
    def test_developer_update_unauthenticated(self):
        """
        Prueba la actualización de un desarrollador sin autenticación.
        """
        self.client.credentials()  # Eliminar la autenticación
        data = {
            "name": "Ubisoft Unauthenticated Update",
            "description": "Unauthenticated update",
            "country": "Germany",
            "web_site": "https://www.ubisoft.de"
        }
        response = self.client.put(
            reverse('developer-detail', kwargs={'pk': self.developer.pk}),
            data
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_developer_delete_unauthenticated(self):
        """
        Prueba la eliminación de un desarrollador sin autenticación.
        """
        self.client.credentials()  # Eliminar la autenticación
        response = self.client.delete(
            reverse('developer-detail', kwargs={'pk': self.developer.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_developer_update_not_found(self):
        """
        Prueba la actualización de un desarrollador que no existe.
        """
        data = {
            "name": "Non-existent Developer",
            "description": "This should fail",
            "country": "USA",
            "web_site": "https://www.example.com"
        }
        response = self.client.put(
            reverse('developer-detail', kwargs={'pk': 999}),  # ID que no existe
            data
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_developer_delete_not_found(self):
        """
        Prueba la eliminación de un desarrollador que no existe.
        """
        response = self.client.delete(
            reverse('developer-detail', kwargs={'pk': 999})  # ID que no existe
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)