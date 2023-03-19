from cgi import print_exception
import pandas as pd 
excel = pd.ExcelFile("DropShipDateta.xlsx")
fj = pd.read_excel(excel, "Fashion Jewelry")
mw = pd.read_excel(excel, "Men's Watches")
ha = pd.read_excel(excel, "Home Appliances")
t = pd.read_excel(excel, "Toys")
sme = pd.read_excel(excel, "Sports and Music Equipment")
oss = pd.read_excel(excel, "Office and School Supplies")

database = [fj,mw,ha,t, sme,oss]

for i in database:
    print (i)


while True:
    inp = input("")

4.9 15 $21.3
5.0 15 $23.3


total for p1 + 0 + 0 + 1 x 1.5 

totl for p2 + 1 + 0 + 0

1.5 > 1.0 



