# in mygame/web/story.py

from django.shortcuts import render

def storypage(request):
    return render(request, "story.html")
