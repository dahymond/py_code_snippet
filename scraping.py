# # Import libraries
# import requests
# import urllib.request
# import time
# from bs4 import BeautifulSoup

# # Set the URL you want to webscrape from
# url = 'http://candidate.fot.com.ng/'

# # Connect to the URL
# response = requests.get(url)

# # Parse HTML and save to BeautifulSoup object
# soup = BeautifulSoup(response.text, "html.parser")

# # To download the whole data set, let's do a for loop through all a tags
# for i in range(36,len(soup.findAll('a'))+1): #'a' tags are for links
#     one_a_tag = soup.findAll('a')[i]
#     link = one_a_tag['href']
#     download_url = 'http://candidate.fot.com.ng/'+ link
#     urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 
#     time.sleep(1) #pause the code for a sec


from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
