import requests
from bs4 import BeautifulSoup

price_list = []
item_list = []
urls = []

domain = "https://www.toolstation.com/"
total_price = 0
item = "10121"
items = [62380,	43424,	10121,	28484,	83455,	21467,	52489,	66137,	89084,	78173,	29607,	81698,	22015,	41043,	53667,	86578,	23000,	98710,	52079,	21966,	45731,	51466,	76952,	48850,	14332,	86362,	82496,	44377,	78751,	46459,	82410,	12218,	12288,	51064,	34883,	60332,	13819,	12869,	66512, 71044, 64596]


for product in items:

    full_address = domain + "p" + str(product)
    print(full_address)
    urls.append(full_address)
    page = requests.get(full_address)

    soup = BeautifulSoup(page.content, "html.parser")

    #spans = soup.find_all('span', {'class': 'font-bold text-[28px] md:text-size-9'})

    price = soup.find(class_="font-bold text-[28px] md:text-size-9").get_text()
    item_name = soup.find(id="videoly-product-title").get_text().strip()

    price_without_currency = price.split("£")[1]
    price_as_float = float(price_without_currency)
    print(price_as_float)
    total_price += price_as_float
    print(total_price)
    print(f'Item: {item_name}, Cost: {price_as_float}, Total: {total_price}')
    price_list.append(price_as_float)
    item_list.append(item_name)

print(price_list)
print(item_list)
print(urls)



#data-pp-amount=

