#!usr/bin/python
# Description: List Comprehensions in buildConnectionString, Step by Step

params = {"server":"mpilgrim","database":"master","uid":"sa","pwd":"secret"}

print params.items()


print [k for k, v in params.items()]
print ";".join([k for k, v in params.items()])

print [v for k, v in params.items()]

print ["%s=%s" % (k,v) for k, v in params.items()]

print ";".join(["%s=%s" % (k,v) for k, v in params.items()])
