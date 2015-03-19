#!usr/bin/env python
# Parsing XML from a string (the file-like object way)

import StringIO
from xml.dom import minidom

contents = "<grammar><ref id='bit'><p>0</p><p>1</p></ref></grammar>"

ssock = StringIO.StringIO(contents)

xmldoc = minidom.parse(ssock)
ssock.close()

print xmldoc.toxml()
