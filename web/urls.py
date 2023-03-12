"""
This is the starting point when a user enters a url in their web browser.

The urls is matched (by regex) and mapped to a 'view' - a Python function or
callable class that in turn (usually) makes use of a 'template' (a html file
with slots that can be replaced by dynamic content) in order to render a HTML
page to show the user.

This file includes the urls in website, webclient and admin. To override you
should modify urls.py in those sub directories.

Search the Django documentation for "URL dispatcher" for more help.

"""
from django.urls import include, path

# default evennia patterns
from evennia.web.urls import urlpatterns as evennia_default_urlpatterns

# add patterns
urlpatterns = [
    # website
    path("", include("web.website.urls")),
    # webclient
    path("webclient/", include("web.webclient.urls")),
    # web admin
    path("admin/", include("web.admin.urls")),
    # add any extra urls here:
    # path("mypath/", include("path.to.my.urls.file")),
]

# 'urlpatterns' must be named such for Django to find it.
urlpatterns = urlpatterns + evennia_default_urlpatterns




"""
Url definition file to redistribute incoming URL requests to django
views. Search the Django documentation for "URL dispatcher" for more
help.

"""
"""
from django.conf.urls import url, include

# default evennia patterns
from evennia.web.urls import urlpatterns

# eventual custom patterns
from web import story
from web import game
from web import codex

custom_patterns = [
    # url(r'/desired/url/', view, name='example'),
    url(r'story', story.storypage, name='Story'),
    url(r'game/new', game.newpage, name='New'),
    url(r'game/prologue', game.prologuepage, name='Prologue'),
    url(r'game/faq', game.faqpage, name='FAQ'),
    url(r'game/participate', game.participatepage, name='Participate'),
    url(r'codex/termsofuse', codex.termsofusepage, name='TermsOfUse'),
    url(r'codex/descriptor', codex.descriptorpage, name='Descriptor'),
    url(r'codex/developer', codex.developerpage, name='Developer'),
    url(r'codex/admins', codex.adminspage, name='Admins'),
    url(r'codex/codesofconduct', codex.codesofconductpage, name='CodesOfConduct'),
    url(r'codex/rights', codex.rightspage, name='Rights'),
    #url(r"^$", website_views.EvenniaIndexView.as_view(), name="index"),
    #url('notifications/', include('django_nyt.urls')),
    #url(r'^wiki/', include('evennia_wiki.urls'), name='Wiki'),
    url(r'^wiki/', include('evennia_wiki.urls')),
	url(r'^boards/', include('paxboards.urls', namespace='board')),
]

# this is required by Django.
urlpatterns = custom_patterns + urlpatterns
"""