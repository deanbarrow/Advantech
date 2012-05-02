#!/usr/bin/python
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup
from sys import argv

if len(argv) == 2:
    script, serial = argv
else:
    print 'Usage: warranty.py [serial]'
    exit(0)
    
def Warranty_Lookup(serial):
    print "\n ", "-" * 26, "\n   Searching for %s\n " % serial, "-" * 26

    url = 'http://erma.advantech.com.tw/Request/warranty_lookup.asp'
    values = {'search_type' : 'Barcode',
              'SearchData' : serial,
              'submit1' : 'Search' }

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    soup = BeautifulSoup(response.read())

    t1 = soup.findAll("td", {"class" : "Table_Title2"})
    t2 = soup.findAll("td", {"class" : "Table_List1_left"})

    for i in range(0,7):
        if t2[i].string:
            t2[i].string = t2[i].string.replace('&nbsp;','')
            
            if t2[i].string:
                print " ", t1[i].string, t2[i].string

    print "\n"
    
Warranty_Lookup(serial)