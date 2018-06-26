import os
import os.path
import time
import logging

# some commands can be executed only if the user's nick is found in this list
owner = list(set([
    'joshmiller'
]))

owner_email = {
    'joshmiller': 'miller.josh@husky.neu.edu',
}

# server to connect to
server = 'irc.quakenet.org' #irc.fold.it
# server's port
port = 6667

# bot's nicknames
nicks = list(set(['JoshBot'])) #FolditIRCBot
# bot's real name
real_name = 'Josh Bot' #Foldit System

# channels to join on startup
channels = list(set([
    '#penguinpi' #global, veteran
]))

cmds = {
    # core commands list, these commands will be run in the same thread as the bot
    # and will have access to the socket that the bot uses
    'core': list(set([
        'quit',
        'join',
        'channels',
    ])),

    # normal commands list, the ones that are accessible to any user
    'user': list(set([
        'task',
        'wiki',
        'answer',
        'about',
        'help',
        'weather',
        'google',
        'mball',
        'uptime',
        'so',
        'twitter',
    ])),

    # commands list that the bot will execute even if a human didn't request an
    # action
    'auto': list(set([
        'email_alert',
    ])),
}

# smtp server for email_alert
smtp_server = 'smtp.gmail.com'
smtp_port = 25
from_email_address = 'Foldit System <folditircmailingsystem@gmail.com>'
from_email_password = 'fol3itir5mail6ngsy8tem'

# users should NOT modify below!
log = os.path.join(os.getcwd(), '..', 'logs', '')
logging_level = logging.DEBUG
start_time = time.time()
current_nick = ''
