# in mygame/web/story.py

from django.shortcuts import render

def almanacpage(request):
    return render(request, "compendium/almanac.html")

def encyclopediapage(request):
    return render(request, "compendium/encyclopedia.html")

def gazettepage(request):
    return render(request, "compendium/gazette.html")

def grimoirepage(request):
    return render(request, "compendium/grimoire.html")

def journalepage(request):
    return render(request, "compendium/journale.html")
