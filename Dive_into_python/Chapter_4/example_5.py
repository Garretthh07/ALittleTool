#!usr/bin/python
# Description: Introducing type

type(1)
print type(1)

li = []
print type(li)

import odbchelper
print type(odbchelper)

import types
print type(odbchelper) == types.ModuleType
