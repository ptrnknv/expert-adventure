from datetime import timedelta
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from store.wsgi import *
from users.models import EmailVerification, User


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.path = reverse('users:register')
        self.data = {'first_name': 'Petr', 'last_name': 'Nikonov', 'username': 'petr24', 'email': 'petr24@mail.ru',
                     'password1': 'Gfdsa321', 'password2': 'Gfdsa321'}
        self.username = self.data['username']

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Регистрация')
        self.assertTemplateUsed(response, 'users/register.html')

    def test_user_registration_post_success(self):
        self.assertFalse(User.objects.filter(username=self.username).exists())
        response = self.client.post(self.path, data=self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        # check creating user
        self.assertTrue(User.objects.filter(username=self.username).exists())
        # check creating email verification
        email_verification = EmailVerification.objects.filter(user__username=self.username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(email_verification.first().expiration.date(), (now() + timedelta(2)).date())

    def test_user_registration_post_error(self):
        User.objects.create(username=self.username)  # for pro version
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)
