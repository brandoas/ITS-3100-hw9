#!/usr/bin/env python
#
# send_nrdp.py

# Inspried by

# Copyright (c) 2010-2017 - Nagios Enterprises, LLC.
# Written by: Scott Wilkerson (nagios@nagios.org)
#

import argparse, sys, urllib, cgi
from xml.dom.minidom import parseString

# If only url and token have been provided then it is assumed that data is being piped
xml = "<?xml version='1.0'?>\n<checkresults>\n";
xml += "<checkresult type='service' checktype='service'>"
xml += "<hostname>localhost</hostname>"
xml += "<servicename>SSH</servicename>"
xml += "<state>o</state>"
xml += "<output>OK:Meh Script</output>"
xml += "</checkresult>"
xml += "</checkresults>"


token = "Brando"
url = "http://its-160-144.its.ohio.edu/nrdp/"

params = urllib.urlencode({'token': token.strip(), 'cmd': 'submitcheck', 'XMLDATA': xml});
opener = urllib.FancyURLopener()

f = opener.open(url, params)
retval = parseString(f.read())
for node in retval.getElementsByTagName("status")[0].childNodes:
    if node.nodeType == node.TEXT_NODE:
	print node.data
