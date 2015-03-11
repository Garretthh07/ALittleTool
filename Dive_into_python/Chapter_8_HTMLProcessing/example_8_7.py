#!usr/bin/python
# Using urllister.py

import urllib, urllister                                 #
usock = urllib.urlopen("https://github.com/Garretthh07") #
parser = urllister.URLLister()                           #
parser.feed(usock.read())                                # 1 : feed defined in SGMLPrser
usock.close()                                            # 2
parser.close()                                           # 3
for url in parser.urls:                                  # 4
    print url                                            #
