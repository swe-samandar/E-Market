from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

# Create your tests here.

class SignUpTestCase(TestCase):
    def test_signup_view(self):
        response = self.client.post(
            reverse('users:signup'),
            data = {
                'first_name': 'Samandar',
                'username': 'samandar',
                'email': 'samandarnemataliyev@gmail.com',
                'password': 'powerpassword',
                'confirm_password': 'powerpassword'
            })
        
        print("STATUS:", response.status_code)
        print("FORM ERRORS:", response.context.get('form').errors if response.context else "NO CONTEXT")

        user = CustomUser.objects.get(username='samandar')
        self.assertEqual(user.first_name, 'Samandar')
        self.assertEqual(user.email, 'samandarnemataliyev@gmail.com')
        self.assertTrue(user.check_password('powerpassword'))
        self.assertEqual(response.status_code, 302)

        second_response = self.client.get('/users/samandar/profile')
        # self.assertEqual(second_response.status_code, 200)

        # login
        self.client.login(username='samandar', password='powerpassword')

        # third_response = self.client.post(
        #     reverse('users:profile-edit'),
        #     data = {
        #         'username': 'shohjahon',
        #         'first_name': 'Shohjahon',
        #         'email': 'nurxonov@gmail.com',
        #         'phone_number': '+998912345678',
        #         'tg_username': 'shohjahon_oken',
        #         'avatar': 'image.jpg'
        #         })
        
        
        # self.assertEqual(user.first_name, 'Shohjahon')
        # self.assertNotEqual(user.first_name, 'Samandar')
        # self.assertEqual(user.tg_username, 'shohjahon_oken')
        # self.assertEqual(user.phone_number, '+998912345678')
        # self.assertEqual(user.email, 'nurxonov@gmail.com')
        # self.assertEqual(user.avatar, 'image.jpg')
        # self.assertEqual(third_response.status_code, 302)