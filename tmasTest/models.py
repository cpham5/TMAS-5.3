from django.db import models

#Create story model for storing storyobjects
class Tmas(models.Model):
    subject = models.TextField()
    date = models.TextField()
    story = models.TextField()
    community = models.TextField()
    user = models.TextField()
    storyID = models.TextField()
    location = models.TextField()


