from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from tmasTest.models import Tmas

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
    user = request.user.get_username()
    location = request.POST['location']
    community = request.POST['community']
    story = Tmas(subject=subject, date=date, story=story, storyID=storyID, user=user, location=location,
                 community=community)
    story.save()
    return HttpResponseRedirect(reverse('index'))