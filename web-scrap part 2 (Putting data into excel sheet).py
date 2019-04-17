
# coding: utf-8

# In[52]:


import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#url link cannot be a google search like https://www.google.com/search?q=drone+flipkart
my_url = 'https://www.alibaba.com/showroom/drone.html'
#connection establish and closed
uReq(my_url)
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#parser is selected as html also html5 and lxml is there 
page_soup = soup(page_html,"html.parser")
#the first one uses page_soup as parser 
#parser.findall("type of tag",{"tag id":"tag id name"})
#returns a list here for example containers
#findall used to find all the tag with a given id name which you need to have knowledge of before hand
containers = page_soup.findAll("div",{"class":"item-main"})
#also the html file can be traversed using '.' operator containers.div

#no of objects found of specific tag
num_of_items = len(containers)


# In[18]:


#for traversing trough all the objects and scraping out the product name
for cont in containers:
    
    pdt_name = cont.div.a.img["alt"]
    print("product name :"+ pdt_name)


# In[21]:


#unconventional way of traversing through html via hierchy 
#hierchy :div class :item-main / div class : item-info / div class : price / span itemprop = "lowPrice"
#                 containers   /             cont_info /    cont_price     /            cont_lowprice
cont = containers[0]
cont_info = cont.findAll("div",{"class":"item-info"})
cont_info0 = cont_info[0]
cont_price = cont_info0.findAll("div",{"class":"price"})
cont_price0 = cont_price[0]
cont_lowprice = cont_info0.findAll("span",{"itemprop":"lowPrice"})
cont_lowprice0=cont_lowprice[0]


# In[54]:


#for the whole tag
print(cont_lowprice0)
#for value inside the tag
print(cont_lowprice0.text)


# In[33]:


#

lows = cont.findAll("span",{"itemprop":"lowPrice"})
print(lows[0].text)
highs = cont.findAll("span",{"itemprop":"highPrice"})
print(highs[0].text)


# In[49]:




for cont in containers:
    
    lows = cont.findAll("span",{"itemprop":"lowPrice"})
    highs = cont.findAll("span",{"itemprop":"highPrice"})
    try :
        print("lowprice"+lows[0].text+"  "+"highprice"+highs[0].text)
#handle no attribute exception which will occur if the specific tag is not pressent int he tag
    except IndexError as e:
        print("nil")
    


# In[ ]:


###############################################################################################################################
                                          ####PART 2####


# In[57]:


#intialise the csv file and a file pointer in write mode
filename = "data.csv"
f = open(filename,"w")


# In[58]:


# define the header or attribute names
# \n is important as it acts as a delimeter 
headers = "product_name , lowest_price , highest_price \n"
f.write(headers)


# In[64]:


filename = "data.csv"
f = open(filename,"w")
headers = "product_name , lowest_price , highest_price\n"
f.write(headers)
for cont in containers:
    pdt_name = cont.div.a.img["alt"] 
    lows = cont.findAll("span",{"itemprop":"lowPrice"})
    highs = cont.findAll("span",{"itemprop":"highPrice"})
    try :
        #writing onto the file
        f.write(pdt_name.replace(",","|") + "," + lows[0].text + "," + highs[0].text + "\n")
    #handle no attribute exception which will occur if the specific tag is not present int he tag
    except IndexError as e:
        print("nil")
f.close()

