import re
import json
import requests

from bs4 import BeautifulSoup


def clean_text(text):
    # Convert TM symbol to Unicode escape sequence
    text = text.replace("\u2122", "™")
    # Remove non-ASCII characters
    cleaned_text = re.sub(r'[^\x00-\x7F]+', '', text)
    # Remove extra whitespace
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text


# URL of the webpage
BASE_URL = "https://www.unox.com/en_gi/"

LINKS_TO_SCRAPE = {
    "commercial_combi_ovens": "ovens/combi/commercial-combi-ovens/",
    "commercial_combi_countertop_ovens": "ovens/combi/commercial-countertop-combi-ovens/",
    "commercial_combi_trolley_ovens": "ovens/combi/commercial-trolley-combi-ovens/",
    "commercial_speed_ovens": "ovens/speed/commercial-speed-ovens/",
    "commercial_speed_combi_ovens": "ovens/speed/commercial-combi-speed-ovens/",
    "commercial_baking_speed_ovens": "ovens/speed/commercial-baking-speed-ovens/",
    "convection_with_humidty": "ovens/convection-with-humidty/commercial-convection-ovens-with-humidity/",
    "commercial_convection_ovens": "ovens/convection/commercial-convection-ovens/",
    "the_hot_fridge": "ovens/hot-preservation-systems/the-hot-fridge/",
    "electric_oven": "ovens/electric/",
    "gas_oven": "ovens/gas/"
}

ALL_PRODUCTS = {}

for key, value in LINKS_TO_SCRAPE.items():
    url = BASE_URL + value

    # Send HTTP GET request to the URL
    response = requests.get(url)

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    product_links = soup.find_all('a', class_='css-p6htja')

    # Find all <div> tags with class 'css-nyyyuv' (these contain product names)
    product_names = soup.find_all('div', class_='css-nyyyuv')

    # Extract the links and names
    links = [link['href'] for link in product_links]
    names = [clean_text(name.get_text(strip=True, separator=" ")) for name in product_names]

    # Combine links and names into a dictionary
    products = dict(zip(names, links))

    # Add the products to the ALL_PRODUCTS dictionary
    ALL_PRODUCTS[key] = products

# store the data in a json file
with open('data/products.json', 'w') as f:
    json.dump(ALL_PRODUCTS, f, indent=4)
