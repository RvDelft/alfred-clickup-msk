from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import datetime
import os

# When a new update is done do the following:
# from NewStoryAddon import isTicketURL  -> main.py rule 21

# 	if isTicketURL(query):
#		return None     -> main.py -> getDueFromInput(query): first check in this method


# Add a space for the : in main.py -> getNameFromInput & getContentFromInput
# to prevent a content added when using a URL


# add :
# 	if (isTicketURL(query)):
#		inputTags.append('ticket')
# to main.py -> getTagsFromInput before the return


# TODO: Fork orginal project and add these changes so new versions can be added via git.

intranetURL = 'intranet.newstory.nl'
jiraURL = 'aanzee.atlassian.net'

def isTicketURL(URL):
    if intranetURL in URL or jiraURL in URL :
        return True  
    else:   
        return False
