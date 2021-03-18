#!/usr/bin/env python
#
# send_nrdp.py

# Inspried by

# Copyright (c) 2010-2017 - Nagios Enterprises, LLC.
# Written by: Scott Wilkerson (nagios@nagios.org)
#

import argparse, sys, urllib, cgi
from xml.dom.minidom import parseString

# The XML portion of the submission.
# Python can conver its internal datastructures "dictionaries" to XML with its built in libraries.
xml = "<?xml version='1.0'?>\n<checkresults>\n";
xml += "<checkresult type='service' checktype='service'>"
xml += "<hostname>localhost</hostname>"
xml += "<servicename>SSH</servicename>"
xml += "<state>o</state>"
xml += "<output>OK:Meh Script</output>"
xml += "</checkresult>"
xml += "</checkresults>"

token = "Schoonover-004"
url = "http://its-160-144.its.ohio.edu/nrdp/"

#Forms that body of the HTTP post message
params = urllib.urlencode({'token': token.strip(), 'cmd': 'submitcheck', 'XMLDATA': xml});

#Defines an object that will manage the http connection.
opener = urllib.FancyURLopener()

#Make the connection to the URL with the parameters
f = opener.open(url, params)

#Check and print the results of the call.
retval = parseString(f.read())
for node in retval.getElementsByTagName("status")[0].childNodes:
    if node.nodeType == node.TEXT_NODE:
	print node.data
