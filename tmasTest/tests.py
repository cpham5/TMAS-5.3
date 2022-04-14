from django.contrib.auth.models import User
from django.test import TestCase, Client

# Create your tests here.
class LoginTestCase(TestCase):
    #tests if a user can login
    def test_login(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

        c = Client()
        logged_in = c.login(username='testuser', password='12345')
        self.assertTrue(logged_in)
        
    def test_create_account(self):
        c = Client()
        response = c.post('/accounts/signup/', {'username': 'chris', 'password1': 'ILoveCMSC447', 'password2': 'ILoveCMSC447'})
    
        logged_in = c.login(username='chris', password='ILoveCMSC447')
        self.assertTrue(logged_in)