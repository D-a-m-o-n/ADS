# from urllib.request import urlopen, Request
# from bs4 import BeautifulSoup
# import pandas as pd
# import openpyxl
# from simplified_scrapy.simplified_doc import SimplifiedDoc
# import xlsxwriter
# url = "https://www.google.com/search?q=Design+Hand-woven+Flower+Pearl+Earrings&rlz=1C1UEAD_enUS941US941&oq=Design+Hand-woven+Flower+Pearl+Earrings&aqs=chrome..69i57j69i60.154j0j7&sourceid=chrome&ie=UTF-8"

# request = Request(url, headers = {'User-agent': 'Mozilla/5.0'})
# html = urlopen(request)
# lis = []
# soup = BeautifulSoup(html, "html.parser")
# ss = soup.find_all("div")
# for i in ss:
#     print (i)


# import requests
# from bs4 import BeautifulSoup
# import argparse

# parser = argparse.ArgumentParser(description='Get Google Count.')
# parser.add_argument('word', help='word to count')
# args = parser.parse_args()

# r = requests.get('http://www.google.com/search',
#                  params={'q':'"'+args.word+'"',
#                          "tbs":"li:1"}
#                 )

# soup = BeautifulSoup(r.text)
# print (soup.find('div',{'id':'resultStats'}).text)

import requests
from bs4 import BeautifulSoup
import pandas as pd 
excel = pd.ExcelFile("DropShipDateta.xlsx")
fj = pd.read_excel(excel, "Fashion Jewelry")
mw = pd.read_excel(excel, "Men's Watches")
ha = pd.read_excel(excel, "Home Appliances")
t = pd.read_excel(excel, "Toys")
sme = pd.read_excel(excel, "Sports and Music Equipment")
oss = pd.read_excel(excel, "Office and School Supplies")
writer = pd.ExcelWriter("DropShipDateta.xlsx",engine = "xlsxwriter")

database = [mw, fj, ha,t, sme,oss]
alisname = ["Office and School Supplies", "Fashion Jewelry", "Men's Watches", "Sports and Music Equipment", "Home Appliances", "Toys"]
counter  = 0

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
for i in database:
    satname = []
    for name in i["name"]:
        if (name != None):
            name = name.replace(" ", "+")
            print (name)
            
            URL     = "https://www.google.com/search?q=" + name
            
            result = requests.get(URL, headers=headers)    

            soup = BeautifulSoup(result.content, 'html.parser')

            total_results_text = soup.find("div", {"id": "result-stats"}).find(text=True, recursive=False) # this will give you the outer text which is like 'About 1,410,000,000 results'
            if(total_results_text != None):
                results_num = ''.join([num for num in total_results_text if (num.isdigit()) ]) # now will clean it up and remove all the characters that are not a number .
                print(results_num)
                satname.append(results_num)
    while len(i) != len(satname):
        satname.append(None)
    i["Saturation"] = satname
    i.to_excel(writer,sheet_name = alisname[counter], index = False)
    counter +=1 
writer.save()

