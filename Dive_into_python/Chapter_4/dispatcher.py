#!usr/bin/python
# Description: Creating a Dispatcher with getattr

import statsout

def output(data, format="text"):
    output_function = getattr(statsout, "output_%s" % format, statsout.output_text)
    return output_function(data)

#if __name__ == "__main__":
#    data  = "This is just a test word"
#    output(data)
