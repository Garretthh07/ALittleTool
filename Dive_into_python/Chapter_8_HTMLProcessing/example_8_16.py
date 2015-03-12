#!usr/bin/python
# Quoting attribute values

htmlSource = """
    <html>
    <head>
    <title>Test page</title>
    </head>
    <body>
    <ul>
    <li><a href=index.html>Home</li>
    <li><a href=toc.html>Table of contents</a></li>
    <li><a href=history.html>Revision history</a></li>
    </body>
    </html>
"""

from BaseHTMLProcessor import BaseHTMLProcessor

parser = BaseHTMLProcessor()
parser.feed(htmlSource)

print parser.output()
