from django.test import TestCase
from app.models.users import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="testuser@example.com",
            username="testuser",
            password="testpass",
            name="Test User",
            dob="1990-01-01",
            cpf="12345678901",
            rg="123456789",
        )

    def test_user_creation(self):
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertEqual(self.user.username, "testuser")
        self.assertTrue(self.user.check_password("testpass"))
        self.assertEqual(self.user.name, "Test User")
        self.assertEqual(str(self.user.dob), "1990-01-01")
        self.assertEqual(self.user.cpf, "12345678901")
        self.assertEqual(self.user.rg, "123456789")

    def test_user_str(self):
        self.assertEqual(str(self.user), "Test User")

    def test_user_email_unique(self):
        with self.assertRaises(Exception):
            User.objects.create_user(
                email="testuser@example.com",
                username="anotheruser",
                password="anotherpass",
            )

    def test_user_cpf_unique(self):
        with self.assertRaises(Exception):
            User.objects.create_user(
                email="anotheruser@example.com",
                username="testuser2",
                password="anotherpass",
                cpf="12345678901",
            )
