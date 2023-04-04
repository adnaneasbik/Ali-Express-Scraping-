import csv 
from bs4 import BeautifulSoup
import requests
from itertools import zip_longest

name = []
price = []
rating = []
links = []


page_num = 0
while True: 
    result = requests.get(f"https://fr.aliexpress.com/w/wholesale-laptop.html?SearchText=laptop&catId=0&initiative_id=SB_20230326085910&spm=a2g0o.productlist.1000002.0&trafficChannel=main&g=y&page={page_num}")
    src = result.content
    soup = BeautifulSoup(src, "lxml")

    if page_num > 50:
        break


    laptops = soup.find_all("a", class_ ="manhattan--container--1lP57Ag cards--gallery--2o6yJVt")
    names = soup.find_all("h1", class_ = "manhattan--titleText--WccSjUS")
    prices = soup.find_all("div", class_ = "manhattan--price-sale--1CCSZfK")
    ratings = soup.find_all("span", class_ = "manhattan--evaluation--3cSMntr")

    for i in range(len(laptops)):
        name.append(names[i].text.strip())
        price.append(prices[i].text.strip())
        try:
            rating.append(ratings[i].text.strip())
        except:
            rating.append('No Info') 
        links.append(laptops[i].attrs['href'].replace('//fr.aliexpress.com/item/', 'https://fr.aliexpress.com/item/'))
    
    page_num += 1 
    print("Next Page")

    file_list = [name, price, rating, links]
    exported = zip_longest(*file_list)
    with open("C:/Users/adnan/OneDrive/Desktop/csv/ali express.csv", "w", encoding='UTF-8') as my_file:
        wr = csv.writer(my_file)
        wr.writerow(["Laptop Name", "Price", "Rating", "Links"])
        wr.writerows(exported) 
        
