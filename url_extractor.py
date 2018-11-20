# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 01:11:53 2018

@author: abhis
"""
#import requests
#import bs4
#res=requests.get('https://www.yelp.com/search?find_desc=&find_loc=Jersey%20City%2C%20NJ')
#print(res.text)
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 16:56:17 2018

@author: abhis
For a location, check the URL of the location before running the code, If location is Los Angeles , add los-angeles in find below code, for las vegas add las-vegas and so on.
"""

from bs4 import BeautifulSoup
import re
import time
import requests

def runforpage(line):
    
    
    html=None
    pgnm=0
    numpage='NA'
    pageLink=line 
    
		
    for i in range(5):# try 5 times
        try:
            #use the browser to access the url
            response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
            html=response.content # get the html
            break # we got the file, break the loop
        except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
            print ('failed attempt',i)
            time.sleep(2) # wait 2 secs
    #print(html) 

     #1   continue # couldnt get the page, ignore
         
    soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html 
        #print(reviews)
    #numpage1=soup.find('div', {'class':re.compile('padding-t-half border-color--default')})
    numpage=soup.find('p', {'class':re.compile('text-align--right')})# get all the review divs
    print(numpage.text)
    #print(numpage)
    #print(numpage.text.split("of",1)[1])
    #print(numpage.text)
    #nmpage=numpage.find('p', {'class':re.compile('text-align--right')})
    pageNum=int(numpage.text.split("of",1)[1])

    pgnm=int(pageNum/10)
    #
    return pgnm

def run(line,pgnm):
    
    #pageNum=10 # number of pages to collect
    #i=i+1
    b=1
    a='https://www.yelp.com'
    
    f=open('LA_City.txt','w') # output file
    prev=''
	
    for p in range(1,pgnm+1): # for each page 
        
        print ('page',p)
        html=None

        if p==1: 
            pageLink=line 
            #print(pageLink) # url for page 1       
        else:
            b=(p-1)
            pageLink=line+'&start='+str(b)+'0'# make the page url
        
        #print(pagelink)
            #print(pageLink)
		
        for i in range(5): # try 5 times
            try:
                #use the browser to access the url
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content # get the html
                break # we got the file, break the loop
            except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                print ('failed attempt',i)
                time.sleep(2) # wait 2 secs
                
        #print(html)
				
        if not html:continue # couldnt get the page, ignore
         
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html 
        
        link=soup.findAll('div', {'class':re.compile('largerScrollablePhotos')}) # get all the review divs
        #print(link)
        for link in soup.find_all('a', href=True):
            if link['href'].startswith('/biz/'): 
                if prev==link['href']:
                    continue
                else:
                    if (link['href'].find('los-angeles') == -1) or (link['href'].find('?') != -1):
                        continue
                    else:
                        #print(link['href'])
                        f.write(a+link['href']+'\n')
                        prev=link['href']      
    f.close()

if __name__=='__main__':
    #i=0    a=0
    line='https://www.yelp.com/search?find_desc=&find_loc=Los%20Angeles%2C%20CA&ns=1'
        #url='https://www.yelp.com/biz/morans-hoboken'
    pgnm=runforpage(line)
    print(pgnm)
    run(line,pgnm)