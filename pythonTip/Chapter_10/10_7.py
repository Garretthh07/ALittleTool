#!usr/bin/env python

# from urllib import urlopen
#
# for line in urlopen('http://tycho.usno.navy.mil/chi-bin/timer.pl'):
#     line = line.decode('utf-8') # Decoding the binary data to text.
#     if 'EST' in line or 'EDT' in line: # look for Eastern Time
#         print(line)

import smtplib

server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar#example.org',
        """To: jcaesar@example.org
        From: soothsayer@example.org

        Beware the Ides of March.
        """)
server.quit()
