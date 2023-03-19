#!/usr/bin/env python
# coding: utf-8

# https://www.jcchouinard.com/web-scraping-with-python-and-requests-html/
# 
# https://pypi.org/project/requests-html/

# In[1]:


import requests
from bs4 import BeautifulSoup as soup
from requests_html import AsyncHTMLSession


# In[2]:


#!pip install pyppdf



# In[3]:


header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}


# In[5]:


html = requests.get('https://www.aliexpress.com/item/32867673917.html?spm=a2g0o.productlist.0.0.3154230d1ytBWE&algo_pvid=6ae5a1f8-b315-44cf-998d-2e38664bd259&algo_expid=6ae5a1f8-b315-44cf-998d-2e38664bd259-0&btsid=0ab6fb8315916032919967411e2635&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_',headers=header,cookies=cookies)


# In[7]:


html.status_code


# In[8]:


cookies = html.cookies


# In[9]:


bsobj = soup(html.content)


# In[10]:


bsobj


# In[11]:


bsobj.findAll('span',{'calss':'product-price-value'})


# In[12]:



asession = AsyncHTMLSession()

r = asession.get('https://www.aliexpress.com/item/32867673917.html?spm=a2g0o.productlist.0.0.3154230d1ytBWE&algo_pvid=6ae5a1f8-b315-44cf-998d-2e38664bd259&algo_expid=6ae5a1f8-b315-44cf-998d-2e38664bd259-0&btsid=0ab6fb8315916032919967411e2635&ws_ab_test=searchweb0_0,searchweb201602_,searchweb201603_')


# In[13]:


r.html.arender()


# In[15]:


h1 = r.html.find('h1')
h1[0].text


# In[16]:


rating = r.html.find('.overview-rating-average')
rating[0].text


# In[19]:


rating_count = r.html.find('.product-reviewer-reviews')
rating_count[0].text.replace('Reviews','').strip()


# In[22]:


price = r.html.find('.product-price-value')
price[0].text.replace('US','').strip()


# In[23]:


r.html.absolute_links

