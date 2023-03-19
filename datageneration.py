from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl
from simplified_scrapy.simplified_doc import SimplifiedDoc
import xlsxwriter
writer = pd.ExcelWriter("DropShipDateta.xlsx",engine = "xlsxwriter")
alisname = ["Office and School Supplies", "Fashion Jewelry", "Men's Watches", "Sports and Music Equipment", "Home Appliances", "Toys"]
alis = ["https://cjdropshipping.com/list/wholesale-office-school-supplies-l-2252588B-72E3-4397-8C92-7D9967161084.html", "https://cjdropshipping.com/list/wholesale-fashion-jewelry-l-123ACC01-7A11-4FB9-A532-338C0E7C04C5.html", "https://cjdropshipping.com/list/wholesale-mens-watches-l-603B4E08-4226-4BFC-A46E-FCCE92ED1C63.html", "https://cjdropshipping.com/list/wholesale-other-sports-equipment-l-36492F79-E7EB-42F0-8DCC-6129BD9D2AE1.html", "https://cjdropshipping.com/list/wholesale-home-appliances-l-85EF081C-819E-448F-BD5C-C5D3F4CFAADA.html","https://cjdropshipping.com/list/wholesale-toys-hobbies-l-04D68B68-1048-4971-BAFA-18FA0A6DB95C.html"]
for url in range(len(alis)):

    request = Request(alis[url], headers = {'User-agent': 'Mozilla/5.0'})
    html = urlopen(request)
    lis = []
    soup = BeautifulSoup(html, "html.parser")
    products = soup.find_all("div", class_ = "product-box")
    pr = products[0].find_all("div", class_ = "inner-box")
    for i in pr:
        linc = []
        for link in i.find_all("a"):
            alink = "https://cjdropshipping.com"+ link.get("href")
            linc.append(alink)
            
            for img in link.find_all("img"):
                image = img.get("src")
                
             
            
        
        pn = i.find_all("div", class_ = "move-box")
        for j in range (len(pn)):        
            pp = pn[j].find_all("div", class_ = "price")
            if len(pp)>0: 
                namefproduct = pn[j].find_all("a", class_ = "desc detail-anchor")
                fproduct = (str(namefproduct[0])) 
                pproduct = (str(pp[0]))
                ind = fproduct.find(">")
                ind2 = pproduct.find(">")
                fproduct = (fproduct[ind+1:])
                fproduct = (fproduct[0:-4])
            
                pproduct = (pproduct[ind2+1:])
                pproduct = (pproduct[0:-6])
                # pdict[fproduct] = [pproduct,linc[0]]
                dictd = {}
                dictd["name"]=fproduct
                dictd["price"]=pproduct
                dictd["link"] = linc[0]    
                dictd["photo"] = image 
                lis.append(dictd)   

    # print (lis)

        df = pd.DataFrame.from_dict(lis)
        df.to_excel(writer,sheet_name = alisname[url], index = False)
writer.save()









    # for i in pdict:
    #     # for j in pdict[i][1]: # looping through all the links 
        
    #     request = Request(pdict[i][1], headers = {'User-agent': 'Mozilla/5.0'})
    #     html = urlopen(request)
    #     soup = BeautifulSoup(html, "html.parser")
    #     doc = SimplifiedDoc(html)
    #     print (doc)
        # tags = soup.find_all("div", id="productDetail")
        # for j in tags:
        #     tabs = soup.find_all("div", class_="pd-con")
        #     print (tabs)
        #     for k in tabs:
        #         taqs = soup.find_all("div", class_="pd-mid")
        #         print (taqs)
        #         for l in taqs:  
        #             taxs = soup.find_all("div", style="min-height: 1100px;")

        #             for o in taxs:
        #                 print(taxs)
        #                 # tas = soup.find("pro-detail")
        #                 # lst = doc.getElementsByTag('ytd-playlist-panel-video-renderer')

        #                 # print (tas)
                    
        #                 break
        #             break
        #         break
        #     break
        # break
            
    
            # print (fproduct)
            # print (pproduct)


            
