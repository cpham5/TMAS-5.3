from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from tmasTest.models import Tmas

import random

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
    #storyID = request.POST['storyID']

    # generate random, unique story id
    currentstoryID = []
    
    stories = Tmas.objects.filter()
    for storyObj in stories:
        currentstoryID.append(getattr(storyObj, 'storyID'))
        
    randID = random.randint(0,1000000)
    while randID in currentstoryID:
        randID = random.randint(0,1000000)
        
    storyID = randID
    

    if request.user.is_authenticated:
        user = request.user.get_username()
    else:
        user = "guest user"
    location = request.POST['location']
    community = request.POST['community']
    status = "Active"
    story = Tmas(subject=subject, date=date, story=story, storyID=storyID, user=user, location=location,
                 community=community, status=status)
    story.save()
    return HttpResponseRedirect(reverse('index'))
    
def addStory(request):
    # not sure if this does anything other than direct the user to the addStory.html page
    return render(request, 'addStory.html')
    
def edit(request, storyID):
    
    # get story with the requested storyID to edit
    story = Tmas.objects.get(storyID=storyID)
    
    # render template and send story to edit template
    return render(request, 'edit.html', {'story': story})
    

# use with form to edit and replace a story
def editReplace(request, storyID):

     # get story with the requested storyID to edit
    story = Tmas.objects.get(storyID=storyID)
    
    # delete old story
    story.delete()   

    # create new story
    subject = request.POST['subject']
    date = request.POST['date']
    story = request.POST['story']
    storyID = storyID
    location = request.POST['location']
    community = request.POST['community']
    user = request.user.get_username()
    status = "Active"
    newStory = Tmas(subject=subject, date=date, story=story, storyID=storyID, user=user, location=location,
                 community=community, status=status)
    newStory.save()
    return HttpResponseRedirect(reverse('index'))

def deleteStory(request, storyID):
    # get story with the requested storyID
    story = Tmas.objects.get(storyID=storyID)
    #deletes story
    story.status = "u_deleted"
    story.save()
    return HttpResponseRedirect(reverse('index'))
    
def adminPage(request):
    stories = Tmas.objects.filter()
    context = {
        'stories': stories,
    }
    return render(request, "admin/adminPage.html", context=context)


def admin(request):
    return render(request, "admin.html")


def delete(request, storyID):
    story = Tmas.objects.get(storyID=storyID)
    story.status = "a_deleted"
    story.save()
    return HttpResponseRedirect(reverse('adminPage'))

def settingsPage(request):
    name1 = request.user.first_name
    name2 = request.user.last_name
    email = request.user.email
    context = {
        "name1":name1,
        "name2":name2,
        "email":email,
    }
    
    return render(request, "registration/settingsPage.html",context=context)

def changeSettings(request):
    request.user.first_name = request.POST.get('newName1', "")
    request.user.last_name = request.POST.get('newName2', "")
    request.user.email = request.POST.get('newEmail', "")
    request.user.save()
    return HttpResponseRedirect(reverse('settingsPage'))

def deleted(request):
    stories = Tmas.objects.filter()
    context = {
        'stories': stories,
    }
    return render(request, "admin/deleted.html", context=context)

def myStories(request):
    stories = Tmas.objects.filter()
    context = {
        'stories': stories,
    }
    return render(request, "myStories.html", context=context)

def aRestore(request, storyID):
    story = Tmas.objects.get(storyID=storyID)
    story.status = "Active"
    story.save()
    return HttpResponseRedirect(reverse('deleted'))

def myDeleted(request):
    stories = Tmas.objects.filter()
    context = {
        'stories': stories,
    }
    return render(request, "myDeleted.html", context=context)

def uRestore(request, storyID):
    story = Tmas.objects.get(storyID=storyID)
    story.status = "Active"
    story.save()
    return HttpResponseRedirect(reverse('myDeleted'))

