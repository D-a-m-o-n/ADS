
import requests
from bs4 import BeautifulSoup
import pandas as pd 




headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}

URL     = "https://cjdropshipping.com/product/wireless-routing-network-card-antenna-p-491B7CE7-F22A-4524-B22A-132CE28871B7.html"
            
result = requests.get(URL, headers=headers)    

soup = BeautifulSoup(result.content, 'html.parser')

