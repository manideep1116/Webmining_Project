# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 13:34:10 2018

@author: Deep Chitroda
"""

from bs4 import BeautifulSoup
import re
import time
import requests


#def getCritic(review):
#    critic,text='NA' # initialize critic and text. NA because sometimes there r no reviews
#    criticChunk=review.find('a',{'href':re.compile('/critic/')})
#    if criticChunk: critic=criticChunk.text#.encode('ascii','ignore'). text in that element is fetched, which is the name
#    return critic
#    
#def getRating(review):
#    rating='NA'
#    ratingChunk=review.find('div',{'class':re.compile('review_icon')})
#    """<div class="review_icon icon small rotten"></div>"""
#    ratingChunk=str(ratingChunk)
#    if(ratingChunk.find('rotten')>0): rating='rotten'
#    if(ratingChunk.find('fresh')>0): rating='fresh'
#    return rating
    
def getTextLen(review):
    textlen='NA'
    textlenChunk=review.find('p',{'lang':re.compile('en')})
    if textlenChunk: textlen=len(textlenChunk.text)
    return textlen
    
def getSource(review):
    source='NA'
    sourceChunk=review.find('li',{'class':re.compile('user-location responsive-hidden-small')})
    if sourceChunk:source=sourceChunk.text
    return source
    
def getDate(review):
    date='NA'
    dateChunk=review.find('span',{'class':re.compile('rating-qualifier')})
    if dateChunk:date=dateChunk.text
    return date



def run(url):

    pageNum=2 # number of pages to collect

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
        #print(html)
        soup = BeautifulSoup(html.decode('ascii', 'ignore'),'html.parser') # parse the html 

        reviews=soup.findAll('div', {'class':re.compile('review review--with-sidebar')}) # get all the review divs

        for review in reviews:

            #critic=getCritic(review)# finds and returns the name of the critic from the given review object

            #rating=getRating(review) # finds and returns the rating from the given review object. The return value should be 'rotten' ,  'fresh', or 'NA' if the review doesn't have a rating.

            source=getSource(review) # finds and returns the source (e.g 'New York Daily News') of the review from the given review object. The return value should be 'NA' if the review doesn't have a source.

            date=getDate(review)  ##finds and returns the date of the review from the given review object. The return value should be  'NA' if the review doesn't have a date.

            textlen=getTextLen(review) # finds and returns the number of characters in the text of the review from the given review object. The return value should 'NA' if the review doesn't have text.
		
            #print(critic, rating, source, date,textlen)
            print(source, date,textlen)

if __name__=='__main__':
    url='https://www.yelp.com/biz/ds-soul-full-cafe-hoboken/'
    run(url)





