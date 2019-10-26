#!/usr/bin/python

import sys
import time
import urllib2
# coding: utf-8
import re
from bs4 import BeautifulSoup
from urlparse2 import urlparse
from O365 import Message
from O365 import Attachment

subject = "TEST SUBJECT"
body = "TEST BODY"
resume = "/Users/Admin/Desktop/EmailScraper-master/SeanMaloneyResume.pdf"

def email(to, subject, body, path):
        authenticiation = ('email','password')
        m = Message(auth=authenticiation)
        m.setRecipients(to)
        m.setSubject(subject)
        m.setBody(body)
        att = Attachment(path=path)
        m.attachments.append(att)
        m.sendMessage()


def execute(to, company):
 email(to, subject+company, body, resume)
 print("Sent To: "+to+" Company: "+company)
### MAIN

def main():
        fileIn = open("emailREFINED.txt","r")
        for line in fileIn.readlines():
                tokens = line.split()
                for i in xrange(len(tokens)-2):
                        execute(tokens[i+2], tokens[0].replace("_", " "))
                        time.sleep(2.5);

main()
