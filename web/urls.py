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
from web.website import game
from web.website import world
from web.website import codex
from web.website import compendium

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
    path(r'game/new', game.newpage, name='New'),
    path(r'game/prologue', game.prologuepage, name='Prologue'),
    path(r'game/maleficent', game.maleficentpage, name='Maleficent'),
    path(r'game/faq', game.faqpage, name='FAQ'),
    path(r'game/participate', game.participatepage, name='Participate'),
    path(r'world/regions', world.regionspage, name='Regions'),
    path(r'world/nations', world.nationspage, name='Nations'),
    path(r'world/guilds', world.guildspage, name='Guilds'),
    path(r'world/craft', world.craftpage, name='Craft'),
    path(r'world/fight', world.fightpage, name='Fight'),
    path(r'world/magic', world.magicpage, name='Magic'),
    path(r'world/quests', world.questspage, name='Quests'),
    path(r'world/seafaring', world.seafaringpage, name='Seafaring'),
    path(r'world/antology', world.antologypage, name='Antology'),
    path(r'codex/termsofuse', codex.termsofusepage, name='TermsOfUse'),
    path(r'codex/descriptor', codex.descriptorpage, name='Descriptor'),
    path(r'codex/developer', codex.developerpage, name='Developer'),
    path(r'codex/admins', codex.adminspage, name='Admins'),
    path(r'codex/codesofconduct', codex.codesofconductpage, name='CodesOfConduct'),
    path(r'codex/privacy', codex.privacypage, name='Privacy'),
    path(r'compendium/almanac', compendium.almanacpage, name='Almanac'),
    path(r'compendium/encyclopedia', compendium.encyclopediapage, name='Encyclopedia'),
    path(r'compendium/gazette', compendium.gazettepage, name='Gazette'),
    path(r'compendium/grimoire', compendium.grimoirepage, name='Grimoire'),
    path(r'compendium/journale', compendium.journalepage, name='Journale'),
    #url(r'^wiki/', include('evennia_wiki.urls')),
	#url(r'^boards/', include('paxboards.urls', namespace='board')),
]

# 'urlpatterns' must be named such for Django to find it.
urlpatterns = urlpatterns + evennia_default_urlpatterns
