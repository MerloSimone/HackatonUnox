import re
import json
import requests

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

ALL_LINKS = {}
ALL_PRODUCTS = {}
# URL of the webpage
BASE_URL = "https://www.unox.com"

# Set up Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # To run Chrome in headless mode

# Set up the Chrome driver
chrome_driver_path = '/Users/farzad/Projects/shitty_jobs/HackatonUnox/crawler/chromedriver'  # Update this with the path to your Chrome driver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)


with open('data/products.json', 'r') as f:
    ALL_PRODUCTS = json.load(f)

for key, value in ALL_PRODUCTS.items():
    print(f"Scraping {key}...")
    products = ALL_PRODUCTS[key]
    ALL_LINKS[key] = {}
    for product_name, product_link in products.items():
        print(f"Scraping {product_name}...")

        url = BASE_URL + product_link

        # Load the webpage
        driver.get(url)
        # Wait for JavaScript to load
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "css-1qr7ipn")))

        # Get the page source after JavaScript is loaded
        page_source = driver.page_source
        # Close the browser
        # # driver.quit()

        soup = BeautifulSoup(page_source, 'html.parser')

        # Find all <div> tags with class 'css-1qr7ipn' (these contain Download area)
        downloadable_section = soup.find_all('div', class_='css-1qr7ipn')
        names = [name.get_text(strip=True, separator=" ") for name in downloadable_section]

        # Find all <div> tags with class 'css-1qr7ipn' (these contain Download links)
        downloadable_links = soup.find_all('div', class_='css-1xdxj46')
        downloadable_links = [dl.find('a')['href'] for dl in downloadable_links]

        links = dict(zip(names, downloadable_links))

        ALL_LINKS[key][product_name] = links

with open('data/links.json', 'w') as f:
    json.dump(ALL_LINKS, f, indent=4)
