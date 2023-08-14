r"""
Evennia settings file.

The available options are found in the default settings file found
here:

/usr/src/evennia/evennia/settings_default.py

Remember:

Don't copy more from the default file than you actually intend to
change; this will make sure that you don't overload upstream updates
unnecessarily.

When changing a setting requiring a file system path (like
path/to/actual/file.py), use GAME_DIR and EVENNIA_DIR to reference
your game folder and the Evennia library folders respectively. Python
paths (path.to.module) should be given relative to the game's root
folder (typeclasses.foo) whereas paths within the Evennia library
needs to be given explicitly (evennia.foo).

If you want to share your game dir, including its settings, you can
put secret game- or server-specific settings in secret_settings.py.

"""

# Use the defaults from Evennia unless explicitly overridden
from evennia.settings_default import *

######################################################################
# Evennia base server config
######################################################################

# This is the name of your game. Make it catchy!
SERVERNAME = "Taltanis"

# Short one-sentence blurb describing your game. Shown under the title
# on the website and could be used in online listings of your game etc.
GAME_SLOGAN = "Hier sind Drachen!"  # "HC SVNT DRACONES"

# Local time zone for this installation. All choices can be found here:
# http://www.postgresql.org/docs/8.0/interactive/datetime-keywords.html#DATETIME-TIMEZONE-SET-TABLE
TIME_ZONE = "Europe/Berlin"
# Activate time zone in datetimes
USE_TZ = True

# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
LANGUAGE_CODE = "de-DE"

# Ändert die verwendete Sprache:
USE_I18N = True
LANGUAGE_CODE = 'de'

# The time factor dictates if the game world runs faster (timefactor>1)
# or slower (timefactor<1) than the real world.
TIME_FACTOR = 13.0

# Different Multisession modes allow a player (=account) to connect to the
# game simultaneously with multiple clients (=sessions). In modes 0,1 there is
# only one character created to the same name as the account at first login.
# In modes 2,3 no default character will be created and the MAX_NR_CHARACTERS
# value (below) defines how many characters the default char_create command
# allow per account.
#  0 - single session, one account, one character, when a new session is
#      connected, the old one is disconnected
#  1 - multiple sessions, one account, one character, each session getting
#      the same data
#  2 - multiple sessions, one account, many characters, one session per
#      character (disconnects multiplets)
#  3 - like mode 2, except multiple sessions can puppet one character, each
#      session getting the same data.
MULTISESSION_MODE = 2

# Whether an account should auto-puppet the last puppeted puppet when logging in. This
# will only work if the session/puppet combination can be determined (usually
# MULTISESSION_MODE 0 or 1), otherwise, the player will end up OOC. Use
# MULTISESSION_MODE=0, AUTO_CREATE_CHARACTER_WITH_ACCOUNT=True and this value to
# mimic a legacy mud with minimal difference between Account and Character. Disable
# this and AUTO_PUPPET to get a chargen/character select screen on login.
AUTO_PUPPET_ON_LOGIN = False # Default: True


######################################################################
# Zusätzliche Komponenten für Webseite und Spiel
######################################################################

#INSTALLED_APPS += (
#        # ...
#        "evennia_wiki",
#		'paxboards',
#)
#
#WIKI_CAN_READ = "anonymous"
#WIKI_CAN_WRITE = "builder"

######################################################################
# In-game Channels created from server start
######################################################################

# The mudinfo channel is a read-only channel used by Evennia to replay status
# messages, connection info etc to staff. The superuser will automatically be
# subscribed to this channel. If set to None, the channel is disabled and
# status messages will only be logged (not recommended).
CHANNEL_MUDINFO = {
    "key": "MudInfo",
    "aliases": "",
    "desc": "Connection log",
    "locks": "control:perm(Developer);listen:perm(Admin);send:false()",
}
# Optional channel (same form as CHANNEL_MUDINFO) that will receive connection
# messages like ("<account> has (dis)connected"). While the MudInfo channel
# will also receieve this info, this channel is meant for non-staffers. If
# None, this information will only be logged.
CHANNEL_CONNECTINFO = None
# New accounts will auto-sub to the default channels given below (but they can
# unsub at any time). Traditionally, at least 'public' should exist. Entries
# will be (re)created on the next reload, but removing or updating a same-key
# channel from this list will NOT automatically change/remove it in the game,
# that needs to be done manually. Note: To create other, non-auto-subbed
# channels, create them manually in server/conf/at_initial_setup.py.
DEFAULT_CHANNELS = [
    # {
    #     "key": "Public",
    #     "aliases": ("pub",),
    #     "desc": "Public discussion",
    #     "locks": "control:perm(Admin);listen:all();send:all()",
    # },
	{
         "key": "Tod",
         "aliases": ("tod",),
         "desc": "Meldung wenn ein Spieler stirbt.",
         "locks": "control:perm(Admin);listen:all();send:all()",
     },
	{
         "key": "Laber",
         "aliases": ("laber","Public","pub"),
         "desc": "Allgemeiner Kanal für Spieler",
         "locks": "control:perm(Admin);listen:all();send:all()",
     },
	{
         "key": "Schwafel",
         "aliases": ("schwafel",),
         "desc": "Allgemeiner Kanal für alle Nicht-Taltanis-Themen",
         "locks": "control:perm(Admin);listen:all();send:all()",
     },
	{
         "key": "Neuling",
         "aliases": ("neuling","neu"),
         "desc": "Kanal für alle Anfänger-Fragen",
         "locks": "control:perm(Admin);listen:all();send:all()",
     },
	{
         "key": "Monster",
         "aliases": ("monster",),
         "desc": "Mitteilung der Monster",
         "locks": "control:perm(Admin);listen:all();send:all()",
     },
	{
         "key": "Nobiles",
         "aliases": ("nobiles",),
         "desc": "Adelige und Götter",
         "locks": "control:perm(Admin);listen:all();send:all()",
     },
	{
         "key": "Pantheon",
         "aliases": ("pantheon",),
         "desc": "Götter unter sich",
         "locks": "control:perm(Admin);listen:perm(Admin);send:perm(Admin)",
     },
]

#######################################################################
# SECRET_KEY
#######################################################################
# This is the signing key for the cookies generated by Evennia's
# web interface.
#
# It is a fallback for the SECRET_KEY setting in settings.py, which
# is randomly seeded when settings.py is first created. If copying
# from here, make sure to change it!
SECRET_KEY = "eZ3czgHfgOi2lJ4NSEBWfUmQamqKN8iHnsfGLmqX"


######################################################################
# Settings given in secret_settings.py override those in this file.
######################################################################
try:
    from server.conf.secret_settings import *
except ImportError:
    print("secret_settings.py file not found or failed to import.")
