#! /usr/bin/env python

import sys, rfc822
import datetime
# Must obtain SNPPlib.py from http://woozle.org/neale/src/python/
import SNPPlib

''' dkmansion
	Description: SNPP client class for Python '''

# Edit strings on line 12, 13, 14, 18, 19, 21, 22 (only if needed, You can delete 21 and 22 if only sending to one user at a time)
SNPPServer = 'snpp.pagingCompany.com'
fromaddr = 'sender@yourCompany.com or just a name'
msgtext = 'Supply your message to the user here ' 

server = SNPPlib.SNPP(SNPPServer)     #localhost
server.set_debuglevel(1)
msg = msgtext + '-'.join(map(str, datetime.datetime.now().timetuple()[:6]))
server.sendpage(fromaddr, ['4321'],msg )

msg = msgtext + '-'.join(map(str, datetime.datetime.now().timetuple()[:6]))
server.sendpage(fromaddr, ['1234'],msg )
server.quit()
