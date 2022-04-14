from tmasTest.models import Tmas
from django.test import TestCase, Client
from django.contrib.auth.models import User

# Create your tests here.

#Add an object (data) to the database for testing
class TmasTestCase(TestCase):
    def setUp(cls):
        cls.foo = Tmas.objects.create(subject="story added from test", date="4/13/2022",
                                      story="Story added from text function", storyID="01234",
                                      user="Moe", location="UMBC", community="TMAS")
    #Test retreving data from database
    def test1(self):
        try:
            flag = 0
            story = self.foo = Tmas.objects.get(storyID="01234")
            if story.date == "4/13/2022":
                if story.subject == "story added from test":
                    if story.story == "Story added from text function":
                        if story.user == "Moe":
                            if story.location == "UMBC":
                                if story.community == "TMAS":
                                    flag = 1
                                    print("***PASS***")
            if(flag == 0):
                print("***FAILED***")
        except Tmas.DoesNotExist:
            print("***FAILED***")


# Create your tests here.
class LoginTestCase(TestCase):
    #tests if a user can log in using the login page
    def test_login(self):
        # creates a test user using the user class
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

        #login to login page using POST
        response = self.client.post('/accounts/login/',{'username':'testuser','password':'12345'}, follow=True)
        self.assertTrue(response.context['user'].is_active)
        
    #creates an account using the account creation page and logs in in using that account
    def test_create_account(self):
        #creates accounts using account creation page
        c = Client()
        response = c.post('/accounts/signup/', {'username': 'chris', 'password1': 'ILoveCMSC447', 'password2': 'ILoveCMSC447'})

        #logs in using Client's login function
        logged_in = c.login(username='chris', password='ILoveCMSC447')
        self.assertTrue(logged_in)
        
        
