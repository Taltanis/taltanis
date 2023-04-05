# in mygame/web/story.py

from django.shortcuts import render

def newpage(request):
    return render(request, "game/new.html")

def prologuepage(request):
    return render(request, "game/prologue.html")

def faqpage(request):
    return render(request, "game/faq.html")

def participatepage(request):
    return render(request, "game/participate.html")

def maleficentpage(request):
    return render(request, "game/maleficent.html")
