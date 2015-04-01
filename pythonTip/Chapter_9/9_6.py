#!usr/bin/env python

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # providdes new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)


test = ['1', '2', '3']
test2 = ['4', '5', '6']
test3 = ['7', '8', '9']

mapTest = MappingSubclass(test)
print "Test Base Class Mapping: ", mapTest.items_list
mapTest.update(test2, test3)
print "MappingSubclass After Update: ", mapTest.items_list

