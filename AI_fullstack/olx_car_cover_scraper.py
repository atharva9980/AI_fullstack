from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time


options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)


url = "https://www.olx.in/items/q-car-cover"
driver.get(url)
time.sleep(5)  # wait for JS to load content


soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()


items = soup.find_all('li', class_='EIR5N')  
results = []

for item in items:
    title = item.find('span', class_='_2tW1I')
    price = item.find('span', class_='_89yzn')
    location = item.find('span', class_='tjgMj')

    if title:
        results.append({
            'Title': title.text.strip(),
            'Price': price.text.strip() if price else 'N/A',
            'Location': location.text.strip() if location else 'N/A'
        })


df = pd.DataFrame(results)
df.to_csv('olx_car_covers.csv', index=False)

print("Saved search results to olx_car_covers.csv")
