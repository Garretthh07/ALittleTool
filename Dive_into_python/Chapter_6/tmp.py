#!usr/bin/python
# Filename: tmp.py

#li = ['a', 'b', 'e']
#for s in li:
#    print s
#
#print "\n".join(li)

#for i in range(5):
#    print i
#
#li = ['a', 'b', 'c', 'd', 'e']
#for  i in range(len(li)):
#    print li[i]

#import os
#for k, v in os.environ.items():
#    print "%s=%s" % (k, v)
#
#print "===================="
#print "\n".join(["%s=%s" % (k,v) for k, v in os.environ.items()])
import os
dirname = "c:\\"

print os.listdir(dirname)

print [f for f in os.listdir(dirname) if os.path.isfile(os.path.join(dirname, f))]

print [f for f in os.listdir(dirname) if os.path.isdir(os.path.join(dirname, f))]
