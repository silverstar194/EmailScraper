#!/usr/bin/python

import sys
import urllib2
import re
from bs4 import BeautifulSoup
from urlparse2 import urlparse
from O365 import Message

def cleanAddress(url):
	http = "http://"
	https = "https://"

	if http in url:
		return url
	elif https in url:
		return url
	else:
		url = "http://" + url
		return url

def parseFromPage(page):
        print(page)
	try:
                req = urllib2.Request(page, headers={'User-Agent' : "Magic Browser"}) 
                website = urllib2.urlopen(req)
		html = website.read()

		addys = re.findall('''[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?''', html, flags=re.IGNORECASE)
		emails.extend(addys)


	except urllib2.HTTPError, err:
		print "Cannot retrieve URL: HTTP Error Code: ", err.code
	except urllib2.URLError, err:
		print "Cannot retrive URL: " + err.reason[1]


def parseFromSite(address):
        print(address)
        req = urllib2.Request(address, headers={'User-Agent' : "Magic Browser"}) 
        url = urllib2.urlopen(req).read()
        soup = BeautifulSoup(url, "lxml")
        for line in soup.find_all('a'):
                o = urlparse(address)
                try:
                        if o.hostname in line.get('href') or '.' not in line.get('href') and line.get('href') is not "":
                                if(o.hostname in line.get('href')):
                                        parseFromPage(line.get('href'))
                                else:
                                        parseFromPage(address+line.get('href'))                               
                except:
                        pass


def execute(url):
        parseFromSite(cleanAddress(url))
        final = [s for s in emails if len(s) <= 35]
        text_file = open("emailsGener8tor.txt", "a")
        out = ' '.join(list(set(final)))
        company = (url[url.index(".") + 1:url.rindex(".")]).title()
        text_file.write(company +" "+ url + " " + out+"\n")
        text_file.close()
        print(list(set(final)))

### MAIN

def main():
        with open("urls.txt", "r") as ins:
            for url in ins:
                try:
                    global emails
                    emails = list()
                    execute(url.rstrip('\n').rstrip('\r'))
                except:
                        pass

        
main()
