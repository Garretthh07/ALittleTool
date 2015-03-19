#!usr/bin/env python
# Parsing XML from a string (the easy but inflexible way)

from xml.dom import minidom

contents = "<grammar><ref id='bit'><p>0</p><p>1</p></ref></grammar>"

xmldoc = minidom.parseString(contents)
print xmldoc.toxml()

