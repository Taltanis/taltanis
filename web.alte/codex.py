# in mygame/web/story.py

from django.shortcuts import render

def termsofusepage(request):
    return render(request, "codex/termsofuse.html")

def descriptorpage(request):
    return render(request, "codex/descriptor.html")

def developerpage(request):
    return render(request, "codex/developer.html")

def adminspage(request):
    return render(request, "codex/admins.html")

def codesofconductpage(request):
    return render(request, "codex/codesofconduct.html")

def rightspage(request):
    return render(request, "codex/rights.html")
