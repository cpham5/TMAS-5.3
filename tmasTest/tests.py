from django.test import TestCase
from tmasTest.models import Tmas

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
            story = self.foo = Tmas.objects.get(storyID="01234")
            if story.date == "4/13/2022":
                if story.subject == "story added from test":
                    if story.story == "Story added from text function":
                        if story.user == "Moe":
                            if story.location == "UMBC":
                                if story.community == "TMAS":
                                    print("***PASS***")
            else:
                print("***FAILED***")
        except Tmas.DoesNotExist:
            print("***FAILED***")


