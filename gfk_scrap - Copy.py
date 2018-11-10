# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 16:56:17 2018

@author: abhis
"""

from bs4 import BeautifulSoup
import re
import time
import requests

def runforpage(line):
    
    
    html=None

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
				
    print(html) 

     #1   continue # couldnt get the page, ignore
         
    soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html 
        #print(reviews)
    numpage=soup.find('div', {'class':re.compile('page-of-pages')}) # get all the review divs
    print(numpage.text.split("of",1)[1])
    pageNum=int(numpage.text.split("of",1)[1])
    return pageNum

def run(line,a,pageNum):
    
    #pageNum=10 # number of pages to collect
    #i=i+1
    b=1
    
    f=open('gfk_'+str(a)+'.txt','w') # output file
	
    for p in range(1,pageNum+1): # for each page 
        
        print ('page',p)
        html=None

        if p==1: 
            pageLink=line 
            print(pageLink) # url for page 1       
        else:
            b=(p-1)*2
            pageLink=line+'?start='+str(b)+'0'# make the page url
            print(pageLink)
		
        for i in range(5): # try 5 times
            try:
                #use the browser to access the url
                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
                html=response.content # get the html
                break # we got the file, break the loop
            except Exception as e:# browser.open() threw an exception, the attempt to get the response failed
                print ('failed attempt',i)
                time.sleep(2) # wait 2 secs
				
		
        if not html:continue # couldnt get the page, ignore
         
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html 
        
        reviews=soup.findAll('div', {'class':re.compile('review--with-sidebar')}) # get all the review divs
        #reviews=soup.findAll('div', {'class':'review-wrapper'})
        #print(reviews)
        if p==1:
            numpage=soup.find('div', {'class':re.compile('page-of-pages')}) # get all the review divs
            print(numpage.text.split("of",1)[1])
            pageNum=int(numpage.text.split("of",1)[1])
        
        
        for review in reviews:
            #print('working')
            text='NA' # initialize critic and text 
            #restChunk=review.find('h1',{'class':re.compile('biz-page-title')})
            #criticChunk=review.find('h1',{'class':re.compile('/critic/')})
            #if restChunk: rest=restChunk.text#.encode('ascii','ignore')
             
            textChunk=review.find('p',{'lang':'en'})
            if textChunk: text=textChunk.text#.encode('ascii','ignore')	
            
            f.write(text+'\n') # write to file
        

    f.close()

if __name__=='__main__':
    #i=0
    a=0
    fw=open('link_jersey.txt','r')
    lines=fw.readlines()
    for line in lines:
        a=a+1
        #url='https://www.yelp.com/biz/morans-hoboken'
        pageNum=runforpage(line)
        run(line,a,pageNum)
    fw.close()
        


