import pandas as pd 
excel = pd.ExcelFile("DropShipDateta.xlsx")
fj = pd.read_excel(excel, "Fashion Jewelry")
mw = pd.read_excel(excel, "Men's Watches")
ha = pd.read_excel(excel, "Home Appliances")
t = pd.read_excel(excel, "Toys")
sme = pd.read_excel(excel, "Sports and Music Equipment")
oss = pd.read_excel(excel, "Office and School Supplies")

database = [mw, fj, ha,t, sme,oss]


ddict = {}
def dg():
    for i in database:
        for index, row in i.iterrows():
            ddict[row[0]] = [row[1], row[2], row[3]]
    return ddict

print (dg())
        








