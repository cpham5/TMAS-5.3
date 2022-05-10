from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from tmasTest.models import Tmas, storyLink, communities

import random

def index(request):
    stories = Tmas.objects.filter()
    links = storyLink.objects.filter()
    context = {
        'stories': stories,
        'links': links,
    }
    return render(request, 'tmasTest/index.html', context=context)

def add(request):
    subject = request.POST['subject']
    date = request.POST['date']
    story = request.POST['story']

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
    comms = communities.objects.filter()
    context = {
        'comms': comms,
    }
    # not sure if this does anything other than direct the user to the addStory.html page
    return render(request, 'addStory.html', context=context)
    
def edit(request, storyID):
    
    # get story with the requested storyID to edit
    story = Tmas.objects.get(storyID=storyID)
    comms = communities.objects.filter()

    # render template and send story to edit template
    return render(request, 'edit.html', {'story': story, 'comms': comms})
    

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

# sets a story to "deleted"
def deleteStory(request, storyID):
    # get story with the requested storyID
    story = Tmas.objects.get(storyID=storyID)
    #deletes story
    story.status = "u_deleted"
    story.save()
    return HttpResponseRedirect(reverse('index'))

# admin page for admins to review stories
def adminPage(request):
    stories = Tmas.objects.filter()
    context = {
        'stories': stories,
    }
    return render(request, "admin/adminPage.html", context=context)

# admin page for admin stuff
def admin(request):
    return render(request, "admin.html")

#deletes a story from adminpage
def delete(request, storyID):
    story = Tmas.objects.get(storyID=storyID)
    story.status = "a_deleted"
    story.save()
    return HttpResponseRedirect(reverse('adminPage'))

# settings page for users to change their name and email
def settingsPage(request):
    name1 = request.user.first_name
    name2 = request.user.last_name
    email = request.user.email
    context = {
        "name1":name1,
        "name2":name2,
        "email":email,
    }
    
    return render(request, "registration/settingsPage.html", context=context)

# changes user's settings
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
    stories = Tmas.objects.filter(user=request.user.get_username())
    links = storyLink.objects.none()
    for story in stories:
        links |= story.links.all()
    links = links.distinct
    context = {
        'stories': stories,
        'links': links,
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

# page to add a link to a story
def linkPage(request, storyID):

    # get story with the requested storyID to add a link to
    story = Tmas.objects.get(storyID=storyID)
    links = storyLink.objects.filter()
    
    # render template and send story to add link template
    return render(request, 'addLink.html', {'story': story, 'links':links})

#adds a link to the story
def addLink(request, storyID):
    story = Tmas.objects.get(storyID=storyID)
    links = storyLink.objects.filter()
    linkName = request.POST.get('link')
    linkSel = request.POST['linkSelect']

    # if the typed input is not empty
    if (linkName!=""):
        # create new link object
        links = storyLink.objects.values_list('title')
        if linkName not in links:
            if linkName == "":
                return render(request, 'addLink.html', {'story': story, 'links':links})
            l = storyLink(title=linkName)
        else:
            for link in links:
                if getattr(link, 'title')==linkName:
                    l = link
    # if the selected input is not empty
    elif(linkSel!=""):
        #get existing link, set to l
        for link in links:
            if getattr(link, 'title')==linkSel:
                l = link
                
    #if both aren't empty, refresh page
    else:
        return render(request, 'addLink.html', {'story': story, 'links':links})
    l.save()
    story.links.add(l)
    story.save()
    return HttpResponseRedirect(reverse('myStories'))

# page to remove a link from a story
def removeLinkPage(request, storyID):
    
    # get story with the requested storyID to remove a link from
    story = Tmas.objects.get(storyID=storyID)
    links = story.links.all()
    
    # render template and send story to remove link template
    return render(request, 'removeLink.html', {'story': story, 'links':links})

# removes a link from a story
def removeLink(request, storyID):
    story = Tmas.objects.get(storyID=storyID)
    linkName = request.POST['link']
    # if a link is selected
    if (linkName!=""):
        # remove link from story
        link = storyLink.objects.get(title=linkName)
        story.links.remove(link)

        # if all links to a story for a StoryLink are gone, delete the storyLink
        if(Tmas.objects.filter(links__title=linkName).count()==0):
            link.delete()
        story.save()
        return HttpResponseRedirect(reverse('myStories'))
    # if a link was not selected
    else:
        # refresh page
        return removeLinkPage(request, storyID)

def addCommunity(request):
    comm = request.POST['comm']
    newCommunity = communities(comm=comm)
    newCommunity.save()
    return HttpResponseRedirect(reverse('manageCommunities'))

def manageCommunities(request):
    comms = communities.objects.filter()
    context = {
        'comms': comms,
    }
    return render(request, "admin/manageCommunities.html", context=context)

def deleteCommunity(request, comm):
    community = communities.objects.get(comm=comm)
    community.delete()
    return HttpResponseRedirect(reverse('manageCommunities'))



