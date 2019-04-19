import bs4
from urllib.request import urlopen as uReq
from urllib.error import HTTPError
from bs4 import BeautifulSoup as soup


check = 'https://www.alibaba.com/showroom/'
count = 0

print("url entered")
my_url = 'https://www.alibaba.com/showroom/rc-car.html'
print("validating URL")
if my_url[0:33] == check:
	try:
		uReq(my_url)
	except HTTPError as e :
		print("Webpage not found")
		exit()

else :
	print("unable to parse :'') Try url like https://www.alibaba.com/showroom/ ")
	exit()



print("initialising connection.......")
#uReq(my_url)
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
print("connection closed")
page_soup = soup(page_html,"html.parser")
containers = page_soup.findAll("div",{"class":"item-main"})
num_of_items = len(containers)

print("initialising excel file....")
filename = "data1.csv"
f = open(filename,"w")
headers = "product_name , lowest_price , highest_price , min amount \n"
f.write(headers)
for cont in containers:
    pdt_name = cont.div.a.img["alt"] 
    lows = cont.findAll("span",{"itemprop":"lowPrice"})
    highs = cont.findAll("span",{"itemprop":"highPrice"})
    amount = cont.findAll("div",{"class":"min-order"})
    try :
        #writing onto the file
        f.write(pdt_name.replace(",","|") + "," + float(lows[0].text) + "," + float(highs[0].text) + ","+ int(amount[0].txt) + "\n")
    #handle no attribute exception which will occur if the specific tag is not present int he tag
    except IndexError as e:
    	count = count+1

print("Attribute missing in ")
print(count)       
print("finishing...")
f.close()
