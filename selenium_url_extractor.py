from selenium import webdriver
import time

#open the browser and visit the url



#scroll down twice to load more tweets
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#time.sleep(2)

def runforpage(line):
#find all elements with a class that ends in 'tweet-text'
#tweets=driver.find_element_by_css_selector("[class$=headerTitle]")
    driver = webdriver.Chrome('./chromedriver')
    driver.get(line)
    #tweet=driver.find_element_by_xpath("""//*[@id="wrap"]/div[3]/div[2]/div[1]/div/div/div[1]/p""")
    tweet=driver.find_element_by_xpath("""//*[@id="wrap"]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/span""")
    factor=driver.find_element_by_xpath("""//*[@id="wrap"]/div[3]/div[2]/div[1]/div/div/div[1]/p""")
    print(tweet.text)
    print(factor.text)
    pageNum=int(tweet.text.split("of",1)[1])
    factorNum=int((factor.text.split("-",1)[1]).split("of")[0])
    pgnm=int(pageNum)
    print(pgnm)
    fact=int(factorNum/10)
    print(fact)
    driver.quit()
    return pgnm,fact

def run(line,pgnm,fact):
    
    #pageNum=10 # number of pages to collect
    #i=i+1
    b=1
    close=False
    #a='https://www.yelp.com'
    
    driver = webdriver.Chrome('./chromedriver')
    
    f=open('Memphis.txt','w') # output file
    prev=''
	
    for p in range(1,pgnm+1): # for each page 
        
        print ('page',p)
        html=None
        url=''
        

        if p==1: 
            pageLink=line 
            #print(pageLink) # url for page 1       
        else:
            b=fact*(p-1)
            pageLink=line+'&start='+str(b)+'0'# make the page url
        print(pageLink)
        driver.get(pageLink)
            #print(pageLink)
        #restLink=driver.find_elements_by_css_selector('[class="lemon--a__373c0__1_OnJ link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5]')
                                                               #lemon--a__373c0__1_OnJ link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5
        #restLink=driver.find_elements_by_xpath("""//*[@id="wrap"]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/ul/li""")
        
                                                   #//*[@id="wrap"]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/ul/li[2]/div/div/div/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/h3/a                     
        #restLink=driver.find_elements_by_class_name("lemon--a__373c0__1_OnJ link__373c0__29943 link-color--blue-dark__373c0__1mhJo link-size--inherit__373c0__2JXk5")
        #print(restLink)
        #if restLink != []:
        for i in range(1,(fact*10)+1): 
            try:
                restLink=driver.find_element_by_xpath("""//*[@id="wrap"]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/ul/li["""+str(i)+"""]/div/div/div/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/h3/a""")
                                                         #//*[@id="wrap"]/div[3]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/ul/li[9]/div/div/div/div/div/div[2]/div[1]/div[1]/div[1]/div[1]/h3/a     
                print(restLink)
                if restLink != []:
                    #link=restLink.find_element_by_xpath("""//*[@href]""")
                    print(type(restLink))
                    print(restLink.get_attribute('href'))
                    if (restLink.get_attribute('href')):
                        if (restLink.get_attribute("href").find('memphis') == -1) or (restLink.get_attribute("href").find('?') != -1):  
                            continue
                        else:
                            url=''
                            url=url+restLink.get_attribute('href')
                            print(url)
                            f.write(url+'\n')
                else:
                    close=True
                    break
            except:
                print('No more restaurants')
                close=True
                break
        if close==True:
            break
            '''print(type(link.get_attribute("href")))
            if link.get_attribute("href").startswith('/biz/'): 
                if prev==link.get_attribute("href"):
                    continue
                else:
                    if (link.get_attribute("href").find('chicago') == -1) or (link.get_attribute("href").find('?') != -1):
                        continue
                    else:
                        #print(link['href'])
                        f.write(a+link.get_attribute("href")+'\n')
                        prev=link.get_attribute("href")'''   
    f.close()
    driver.quit()


if __name__=='__main__':
    #i=0    a=0
    line='https://www.yelp.com/search?find_desc=&find_loc=Memphis%2C%20TN'
        #url='https://www.yelp.com/biz/morans-hoboken'
    pgnm,fact=runforpage(line)
    run(line,pgnm,fact)


# -*- coding: utf-8 -*-
