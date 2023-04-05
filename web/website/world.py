# in mygame/web/story.py

from django.shortcuts import render

def regionspage(request):
    return render(request, "world/regions.html")

def nationspage(request):
    return render(request, "world/nations.html")

def guildspage(request):
    return render(request, "world/guilds.html")

def craftpage(request):
    return render(request, "world/craft.html")

def fightpage(request):
    return render(request, "world/fight.html")

def magicpage(request):
    return render(request, "world/magic.html")

def questspage(request):
    return render(request, "world/quests.html")

def seafaringpage(request):
    return render(request, "world/seafaring.html")
