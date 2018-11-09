# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 01:11:53 2018

@author: abhis
"""
import time
from bs4 import BeautifulSoup
import urllib.request

def make_link(n):
    a = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=Jersey+City%2C++%22&start=" + str(n)
    return a

def open_link(n):
    resp = urllib.request.urlopen(make_link(n))
    return resp

def soupify(n):
    resp = open_link(n)
    soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))
    return soup

yelp = 'https://www.yelp.com'

data = set()
for n in range(511,900):
    soup = soupify(n)
    for link in soup.find_all('a', href=True):
        if link['href'].startswith('/biz/'):
            page = yelp + link['href']
            print(page)
            data.add(page)

with open('urls.txt', 'a') as f:
    for item in data:
        f.write(item)

#import requests
#import bs4
#res=requests.get('https://www.yelp.com/search?find_desc=&find_loc=Jersey%20City%2C%20NJ')
#print(res.text)
#i=511
#a='https://www.yelp.com'
##fw=open('link_jersey2.txt','w') # output file
#prev=''
##resp = urllib.request.urlopen("https://www.yelp.com/search?find_desc=&find_loc=Jersey%20City%2C%20NJ"+"&start="+str(i)+"0")
#while True:
#    i=i+1
#    print(i)
#    #soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))
#    soup = soupify(i)
#
#    for link in soup.find_all('a', href=True):
#        if link['href'].startswith('/biz/'): 
#            if prev==link['href']:
#                continue
#            else:
#                if (link['href'].find('jersey') == -1) or (link['href'].find('?') != -1):
#                    continue
#                else:
#                    #print(link['href'])
#                    print("Adding to file:")
#                    with open('link_jersey2.txt', 'a') as fw:
#                        fw.write(a+link['href']+'\n')
#                    prev=link['href']
#    #time.sleep(5) 
#    #resp = urllib.request.urlopen("https://www.yelp.com/search?find_desc=&find_loc=Jersey%20City%2C%20NJ"+"&start="+str(i)+"0")
##fw.close()
