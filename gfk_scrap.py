# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 16:56:17 2018

@author: abhis
"""

from bs4 import BeautifulSoup
import re
import time
import requests


def run(url):

    pageNum=10 # number of pages to collect
    
    fw=open('ngfk_1.txt','w') # output file
	
    for p in range(1,pageNum+1): # for each page 

        print ('page',p)
        html=None

        if p==1: pageLink=url # url for page 1
        else: pageLink=url+'?page='+str(p)+'&sort=' # make the page url
		
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
        
        reviews=soup.findAll('div', {'class':re.compile('review-content')}) # get all the review divs
        

        for review in reviews:

            text='NA' # initialize critic and text 
            #restChunk=review.find('h1',{'class':re.compile('biz-page-title')})
            #criticChunk=review.find('h1',{'class':re.compile('/critic/')})
            #if restChunk: rest=restChunk.text#.encode('ascii','ignore')
             
            textChunk=review.find('p',{'lang':'en'})
            if textChunk: text=textChunk.text#.encode('ascii','ignore')	
            
            fw.write(text+'\n') # write to file 
		
        

    fw.close()

if __name__=='__main__':
    url='https://www.yelp.com/biz/morans-hoboken'
    run(url)


