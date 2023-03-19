from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
from simplified_scrapy.simplified_doc import SimplifiedDoc
import xlsxwriter

excel = pd.ExcelFile("DropShipDateta.xlsx")
fj = pd.read_excel(excel, "Fashion Jewelry")
mw = pd.read_excel(excel, "Men's Watches")
ha = pd.read_excel(excel, "Home Appliances")
t = pd.read_excel(excel, "Toys")
sme = pd.read_excel(excel, "Sports and Music Equipment")
oss = pd.read_excel(excel, "Office and School Supplies")

database = [fj,mw,ha,t,sme,oss]


for i in range (len(database)):
    linkofp = list(database[i]["link"])
    for j in linkofp:
        print (j)

request = Request(alis[url], headers = {'User-agent': 'Mozilla/5.0'})
html = urlopen(request)
lis = []
soup = BeautifulSoup(html, "html.parser")
products = soup.find_all("div", class_ = "product-box")
pr = products[0].find_all("div", class_ = "inner-box")  