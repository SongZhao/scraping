
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=knife'

uClient = uReq(my_url)
page_html = uCLient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class":"item-container"})
filename = "product_csv"
f = open(filename, "w")
headers = "brand, product_name, shipping\n"

for container in containers
	title_containter = container.findAll("a",{"class":"item-title"})
	brand = container.div.div.a.img["item-title"]
	product_name = title_container[0].text
	shipping_container = container.findAll("li":{"class":"price-ship"})
	shipping = shipping_container[0].text.strip()
	f.write(brand + "," + "product_name.replace(",", "|") + "," + shipping + "\n")

