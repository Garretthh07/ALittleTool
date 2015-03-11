#!usr/bin/python
# Introducting urllib

import urllib
#sock = urllib.urlopen("https://www.baidu.com")
sock = urllib.urlopen("https://github.com/Garretthh07")
htmlSource = sock.read()
sock.close()
print htmlSource
