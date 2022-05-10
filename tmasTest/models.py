from django.db import models

#Create story model for storing storyobjects
class storyLink(models.Model):
    title = models.TextField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Tmas(models.Model):
    subject = models.TextField()
    date = models.TextField()
    story = models.TextField()
    community = models.TextField()
    user = models.TextField()
    storyID = models.TextField()
    location = models.TextField()
    status = models.TextField()
    links = models.ManyToManyField(storyLink)

class userQueue(models.Model):
    storyID = models.TextField()
    relation = models.TextField()
    
class userStoryOptions(models.Model):
    storyID = models.TextField()
    owner = models.TextField()
    visibility = models.TextField()
    #more options later
    
#edit later
class userFriendsList(models.Model):
    user = models.TextField()
