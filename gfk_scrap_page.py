# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 16:56:17 2018

@author: abhis
"""

from bs4 import BeautifulSoup
import re
import time
import requests

def run(line,a):
    
    
    f=open('gfk_'+str(a)+'.txt','w') # output file
	        
    html=None

    pageLink=line 
    print(pageLink) # url for page 1       
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
    
    header=soup.find('h1', {'class':re.compile('biz-page-title')})
    hdr='NA'
    if header: hdr=header.text.strip()
    f.write(''.join(hdr)+'\n')
    
    category=soup.find('div', {'class':re.compile('biz-page-header-left')})
    categoryhdr=category.find('span', {'class':'category-str-list'})
    ctghdr=categoryhdr.findAll('a')
    for ctghd in ctghdr:
        ctg='NA'
        #ctgChunk=ctghd.find('a')
        ctg=ctghd.text
        f.write(ctg+'\t')
    f.write('\n')
        #f.write(''.join(hdr)+'\n')
        
    #timings=soup.find('div', {'class':re.compile('column-beta')})
    for i in range(0,7):
        for tr in soup.find('tr')[i]:
            tds=tr.find('td')
            uls=tr.find('li')
            lis=tr.find('div')
            divs=tr.find('p')
            print(divs.text)
    #    timedaily='NA'
    #    timeChunk=timing.findAll('td')
    #    if timeChunk: timedaily=timeChunk.text
    #    print(timedaily)
    #    f.write(timedaily+'\n')
    
    binfos=soup.find('div', {'class':'bordered-rail'})
    binfo=binfos.find('ul', {'class':'ylist'})
    attributes=binfo.findAll('dl')
    #print(attributes)
    for attribute in attributes:
        #print('working')
        point,comment='NA','NA' # initialize critic and text 
         
        pointChunk=attribute.find('dt', {'class':'attribute-key'})
        if pointChunk: point=pointChunk.text.strip()#.encode('ascii','ignore')
        commentChunk=attribute.find('dd')
        if commentChunk: comment=commentChunk.text.strip()
        #.encode('ascii','ignore')	
        if ''.join(point) == 'Good for Kids':
            continue
        else:
            f.write(''.join(point)+'\t'+''.join(comment)+'\n') # write to file
     
    #soup = BeautifulSoup(html.decode('ascii', 'ignore'),'lxml') # parse the html 
    
    reviews=soup.findAll('div', {'class':re.compile('review--with-sidebar')}) # get all the review divs
    for review in reviews:
        #print('working')
        text='NA' # initialize critic and text 
         
        textChunk=review.find('p',{'lang':'en'})
        if textChunk: text=textChunk.text#.encode('ascii','ignore')	
        f.write(text+'\n') # write to file
    

    f.close()

if __name__=='__main__':
    #i=0
    a=0
    fw=open('link_jersey_1.txt','r')
    lines=fw.readlines()
    for line in lines:
        a=a+1
        #url='https://www.yelp.com/biz/morans-hoboken'
        #pageNum=runforpage(line)
        run(line,a)
    fw.close()
        


