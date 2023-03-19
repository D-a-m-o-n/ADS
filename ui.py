import random
from cgi import print_exception
import pandas as pd 
from operator import itemgetter
import math 
import nltk
nltk.download('averaged_perceptron_tagger')
from nltk import word_tokenize, pos_tag
excel = pd.ExcelFile("DropShipDateta.xlsx")
fj = pd.read_excel(excel, "Fashion Jewelry")
mw = pd.read_excel(excel, "Men's Watches")
ha = pd.read_excel(excel, "Home Appliances")
t = pd.read_excel(excel, "Toys")
sme = pd.read_excel(excel, "Sports and Music Equipment")
oss = pd.read_excel(excel, "Office and School Supplies")

database = [fj,mw,ha,t,sme,oss]

shiptime = {'15': 0.05, '18' : 0.075, '20' : 0.08, '23' : 0.1, '25' : 0.12, '26' : 0.125, '28' : 0.15, '30' : 0.3}

def weightrand (weights):
    choice = random.choices(list(weights.keys()), weights = list(weights.values()))
    return choice[0]



# for i in database:
#     print (i)

adjl = []
for i in range (len(database)):
    ajd = {}
    plist = database[i]
    nameofp = list(plist["name"])
    for i in range (len(nameofp)):
        namesent = nameofp[i]
        words = nltk.word_tokenize(namesent)
        tagged_words = nltk.pos_tag(words)
        adjectives = tuple([word[0].upper() + word[1:].lower() for word, pos in tagged_words if pos == "JJ"])
        if (adjectives != []):
            ajd[adjectives] = namesent
       
    adjl.append(ajd)    

def hashtags (adj):
    adj = adj[0].upper() + adj[1:].lower()
    itadjl = []
    for i in adjl:
        for j in i.keys():
            if (adj in j):
                itadjl.append(i[j])
    return (itadjl)

print (hashtags("crEATivE"))

def logd(price, l=1.5, k = 0.83333, et = 0.0534):
    return l/(1-(k*(math.e**(et*-price))))

# print (logd(10000))



Category = database[5]
pndict = {list(Category["name"])[k]:list(Category["price"])[k] for k in range (len(list(Category["price"])))}
    
for i in pndict:
    if (type(pndict[i]) == float):
        pndict[i] = "$" + str(pndict[i])
    if ("-" in pndict[i]):
        pndict[i] = pndict[i][1:]
        pndict[i] = pndict[i].split("-")
        pndict[i] = [float(j) for j in pndict[i]]

    else:
        pndict[i] = float(pndict[i][1:])

while True: 
    print ("Please pick an option from below:")
    print("1: Fashion Jewelry\n2: Men's Watches\n3: Home Appliances\n4: Toys\n5: Sports and Music Equipment\n6: Office and School Supplies")
    print ("Type 'quit' to quit")
    input1 = int(input ("---")) - 1
    
    
    Category = database[input1]
 
    if (input1 =="quit"):
        quit()

    print ("Please pick an option from below:")
    print ("1: List of Best Prices")
    print ("2: List of Best Shipping Time")
    print ("3: List of Lowest Satuation")
    print ("4: Custom List")
    print ("Type 'quit' to quit")
    inp = input("---")
    
    
    if (inp == "1"): ## liat of best p
        pndict = {list(Category["name"])[k]:list(Category["price"])[k] for k in range (len(list(Category["price"])))}
            
        for i in pndict:
            if (type(pndict[i]) == float):
                pndict[i] = "$" + str(pndict[i])
            if ("-" in pndict[i]):
                pndict[i] = pndict[i][1:]
                pndict[i] = pndict[i].split("-")
                pndict[i] = [float(j) for j in pndict[i]]
    
            else:
                pndict[i] = float(pndict[i][1:])
    
        pdict = {}
        
        for z in pndict:
            if (type(pndict[z]) != float):
                avg = round((pndict[z][0]+pndict[z][1])/2,2)
                pdict[avg] = pndict[z]
                pndict[z] = avg
        
        
        cs = sorted(pndict.items(),key = lambda item:item[1])
        nl = cs.copy()
        totalc = cs[len(cs) - 1][1] + cs[0][1]

        for i in range(len(cs)):
            cs[i] = list(cs[i])
            cs[i][1] = cs[i][1]/totalc
            cs[i][1] = (100-(cs[i][1]*100))
        
        for i in range(10):
            rr = (round(logd(nl[i][1]), 2))
            # print ("#" + str(i) + " " + nl[i][0] + " " + "$"+str(nl[i][1]))
            print (f"#{i}. {nl[i][0]} | ${nl[i][1]} | RRP ${round(rr*(nl[i][1]), 2)} (%{int(100*(rr))} Estimate Profit)| ")
            # print(cs[len(cs)-i-1][0], ((totalc*cs[len(cs)-i-1][1])/100))
        


    if (inp == "2"): ## list of best st 
        pass
    
    if (inp == "3"): ## list of best s 
        satlis = {}
        ## thisdict["color"] = "red"
        
        name = list(Category["name"])
        satuaration = list(Category["Saturation"])

        for i in range(len(name)):

            satlis[name[i]] = satuaration[i]
        satlist = sorted(satlis.items(),key = lambda item:item[1])
        # gs = satlist[len(satlist) - 1][1] 
        print (satlist[0])
        totalq = satlist[0][1] + satlist[len(satlist) - 1][1] 
        for i in range(len(satlist)):
            satlist[i] = list(satlist[i])
            # satlist[i][1] = satlist[i][1]/gs
            satlist[i][1] = satlist[i][1]/totalq
        print (satlist)

    if (inp == "4"): ## list of best cl
        pndict = {list(Category["name"])[k]:list(Category["price"])[k] for k in range (len(list(Category["price"])))}
            
        for i in pndict:
            if (type(pndict[i]) == float):
                pndict[i] = "$" + str(pndict[i])
            if ("-" in pndict[i]):
                pndict[i] = pndict[i][1:]
                pndict[i] = pndict[i].split("-")
                pndict[i] = [float(j) for j in pndict[i]]
    
            else:
                pndict[i] = float(pndict[i][1:])
    
        pdict = {}
        for z in pndict:
            if (type(pndict[z]) != float):
                avg = round((pndict[z][0]+pndict[z][1])/2,2)
                pdict[avg] = pndict[z]
                pndict[z] = avg
        
        cs = sorted(pndict.items(),key = lambda item:item[1])
        totalc = cs[len(cs) - 1][1] + cs[0][1]
        for i in range(len(cs)):
            cs[i] = list(cs[i])
            cs[i][1] = cs[i][1]/totalc
            cs[i][1] = (100-(cs[i][1]*100))
        satlis = {}
        ## thisdict["color"] = "red"
        
        name = list(Category["name"])
        satuaration = list(Category["Saturation"])

        for i in range(len(name)):

            satlis[name[i]] = satuaration[i]
        satlist = sorted(satlis.items(),key = lambda item:item[1])
        gs = satlist[len(satlist) - 1][1] 
        ls = satlist[0][1]
        for i in range(len(satlist)):
            satlist[i] = list(satlist[i])
            satlist[i][1] = satlist[i][1]/(gs+ls)
        total = []
        print (satlist)
        for i in satlist:
            for j in cs:
                if(i[0] == j[0]):
                    tlis = []
                    tlis.append(i[0])
                    tlis.append(i[1]+j[1])
                    total.append(tlis)
        total = sorted(total, key = itemgetter(1))
        print (total)
        
    





            
