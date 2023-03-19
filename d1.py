from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.amazon.com/gp/bestsellers/books/11892"
request = Request(url, headers = {'User-agent': 'Mozilla/5.0'})
html = urlopen(request)

soup = BeautifulSoup(html, "html.parser")
book = soup.find_all("div", id = "gridItemRoot") 
for i in book:
    print ( i.prettify())
    rank = i.find("span", class_ = "zg-bdg-text").get_text().replace("#", "")
    title = i.find("span", class_ = "_cDEzb_p13n-sc-css-line-clamp-1_1Fn1y").get_text()
    print (rank)
    print (title)
    print("\n\n\n\n\n\n\n\n")
    
    