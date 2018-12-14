from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from model_mommy import mommy
from . import models

class TestsSetUp(APITestCase):
    def setUp(self):
        self.client = APIClient()
        User.objects.create_user(username='testuser', email='test@test.com', password='testpass12')
        test_user = User.objects.create_user(username='testuser1', email='test1@test.com', password='testpass12')
        self.user = User.objects.get(username='testuser1')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)


class UserAuthTests(TestsSetUp):
    '''Authentication related tests'''
    def test_admin_login_successful_with_valid_credentials(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass12'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_admin_login_with_wrong_credentials_fail(self):
        response = self.client.post(reverse('login'), {'username': 'wrongusername', 'password': 'wrongone'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class CategoriesTests(TestsSetUp):
    '''tests related to categories'''
    def test_admin_can_create_a_category(self):
        response = self.client.post(reverse('create_category'), {'name': 'testcategory'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_category_creation_requires_login(self):
        unauthorized_client = APIClient()
        response = unauthorized_client.post(reverse('create_category'), {'name': 'testcategory'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED )

    def test_admin_can_edit_a_category(self):
        mommy.make(models.Categories, name='testcategory2')
        response = self.client.patch(reverse('category_details', kwargs={'pk': 1}), {'name': 'new category name'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('new category name', response.data['name'])

    def test_admin_can_delete_a_category(self):
        mommy.make(models.Categories)
        response = self.client.delete(reverse('category_details', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response.data, None)
