import requests
from bs4 import BeautifulSoup


domain = "https://www.toolstation.com/"

item = "10121"

full_address = domain + "p" + item

print(full_address)

page = requests.get(full_address)

soup = BeautifulSoup(page.content, "html.parser")

spans = soup.find_all('span', {'class': 'font-bold text-[28px] md:text-size-9'})



#data-pp-amount=

