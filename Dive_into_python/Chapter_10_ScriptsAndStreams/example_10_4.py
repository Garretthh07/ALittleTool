#!usr/bin/env python
# Introducing StringIo

contents = "<grammar><ref id='bit'><p>0</p><p>1</p></ref></grammar>"

import StringIO

ssock = StringIO.StringIO(contents)

print ssock.read()
print ssock.read()
print ssock.seek(0)
print ssock.read(15)
print ssock.read(15)
print ssock.read()

ssock.close()
