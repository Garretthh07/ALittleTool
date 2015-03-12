#!usr/bin/python
# Introducing globals

if __name__ == "__main__":
    for k,v in globals().items():
        print k, "=", v
