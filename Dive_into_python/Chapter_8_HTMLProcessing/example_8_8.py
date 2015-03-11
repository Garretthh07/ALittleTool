#!usr/bin/python
# Introducing  BaseHTMLProcessor

from sgmllib import SGMLParser
import htmlentitydefs

class BaseHTMLProcessor(SGMLParser):
    def reset(self): # 1
        self.pieces = []
        SGMLParser.reset(self)

    def unknown_starttag(self, tag, attrs): # 2
        strattrs = "".join([' %s="%s"' % (key,value) for key, value in attrs])
        self.pieces.append("<%(tag)s%(strattrs)s>" % locals())

    def unknown_endtag(self, tag): # 3
        self.pieces.append("</%(tag)s>" % locals())

    def handle_charref(self, ref): # 4
        self.pieces.append("&#%(ref)s;" % locals())

    def handle_entityref(self, ref): # 5
        self.pieces.append("&%(ref)s" % locals())
        if htmlentitydefs.entitydefs.has_key(ref):
            self.pieces.append(";")

    def handle_data(self, text): # 6
        self.pieces.append(text)

    def handle_comment(self, text): # 7
        self.pieces.append("<!--%(text)s-->" % locals())

    def handle_pi(self, text): # 8
        self.pieces.append("<?%(text)s>" % locals())

    def handle_decl(self, text):
        self.pieces.append("<!%(text)s>" % locals())

    def output(self):
        """ Return processed HTML as a single string """
        return "".join(self.pieces)

