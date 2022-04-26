from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from tmasTest.models import Tmas

#import random
#import sqlite3

def index(request):
    stories = Tmas.objects.filter()
    context = {
        'stories': stories,
    }
    return render(request, 'tmasTest/index.html', context=context)

def add(request):
    subject = request.POST['subject']
    date = request.POST['date']
    story = request.POST['story']
    storyID = request.POST['storyID']
#randID = random.randint(0,1000000)
#conn = sqlite3.connect(djano.db')
#cursor = conn.cursor()
#data=cursor.execute('''SELECT storyID FROM Tmas''')
#currentStoryIds = []
#    for id in data
#	currentstoryIDs.append(id) 	
#    while randID in currentStoryIds
#	randID = random.randint(0, 1000000)
#    storyID = randID
#    conn.commit()
#    conn.close()

    if request.user.is_authenticated:
        user = request.user.get_username()
    else:
        user = "guest user"
    location = request.POST['location']
    community = request.POST['community']
    story = Tmas(subject=subject, date=date, story=story, storyID=storyID, user=user, location=location,
                 community=community)
    story.save()
    return HttpResponseRedirect(reverse('index'))
    
def edit(request, storyID):
    #return HttpResponse(storyID)
    
    # get story with the requested storyID to edit
    story = Tmas.objects.get(storyID=storyID)
    
    # render template and send story to edit template
    return render(request, 'edit.html', {'story': story})
    
