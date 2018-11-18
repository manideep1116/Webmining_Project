from bs4 import BeautifulSoup
import requests

page_url = 'https://www.yelp.com/search?cflt=restaurants&find_loc=San%20Jose%2C%20CA&start=0'
save_file = '/home/manideep/Downloads/webmining_project/myfile1'

# return next possible yelp page.  If beginning page, don't do anything
def next_page(i, page_url):
    if i == 0:
        return page_url
    return page_url + '&start=' + str(i)

i = 1
while True:
    print("Extracting new page ", i)
    current_url = next_page((i-1) * 30, page_url)
    try:
        resp = requests.get(current_url) # get HTML
    except Exception as e:
        print("error: ", e)
        break

    # parse HTML
    soup = BeautifulSoup(resp.content) 
    # find ALL hrefs in page
    hrefs = set(soup.find_all('a', href=True))
    # filter those hrefs which start with '/biz'
    rests = filter(lambda x: x['href'].startswith('/biz'), hrefs)
    # add url to the href's found
    values = map(lambda x: 'https://www.yelp.com' + x['href'], rests)

    if len(values) == 0:
        print("You can stop now...")

    # save in file
    with open(save_file, 'a') as f:
        for item in values:
            f.write("%s\n" % item)
    i += 1
