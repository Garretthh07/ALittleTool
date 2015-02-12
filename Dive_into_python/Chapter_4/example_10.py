#!usr/bin/python
# Description: Introducing getattr

li = ["Larry", "Curly"]
print li.pop

print getattr(li, "pop")

getattr(li, "append")("More")

print li

print getattr({}, "clear")

getattr((), "pop")
