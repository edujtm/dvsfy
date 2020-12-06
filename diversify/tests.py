from django.test import TestCase
from django.contrib import auth
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.logged_user = User.objects.create_user(username='random-user', password='secret-password')

    def test_logged_out_user_should_arrive_at_landing_page(self):
        response = self.client.get('/');
        self.assertTemplateUsed(response, 'index.html')

    def test_logged_out_user_cannot_access_app(self):
        response = self.client.get('/app/')
        self.assertRedirects(response, expected_url='/');

    def test_logout_already_logged_out_is_noop(self):
        # Given: an logged out user
        response = self.client.get('/app/logout')

        # Then: the user should only be redirected
        self.assertRedirects(response, '/')

    def test_redirects_logged_in_user_to_app(self):
        user = self.logged_user
        self.client.force_login(user=user)
        response = self.client.get('/')
        self.assertRedirects(response, expected_url='/app/')

    def test_logged_in_user_can_logout(self):
        # Given: a logged in user
        logged_user = self.logged_user
        self.client.force_login(user=logged_user)

        user = auth.get_user(self.client)
        self.assertTrue(user.is_authenticated)

        # When: the user asks to logout
        response = self.client.get('/app/logout')

        # Then: it should be redirected to landing page
        self.assertRedirects(response, expected_url='/')

        # And: it should not be logged in
        user = auth.get_user(self.client)
        self.assertFalse(user.is_authenticated)
