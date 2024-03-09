import os
import requests
import json


def fix_directory(text):
    # Count the occurrences of "/"
    slash_count = text.count("/")

    if slash_count <= 2:
        return text
    last_slash_index = text.rfind("/")
    return f"{text[:last_slash_index]}_{text[last_slash_index + 1:]}"


# Function to download a file from a URL
def download_file(url, directory, file_name):
    # get the file extension
    file_extension = url.split('.')[-1].split('?')[0]
    download_file_name = os.path.join(directory, f"{file_name}.{file_extension}")
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(download_file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return download_file_name


# Load JSON data
with open('data/links.json', 'r') as file:
    data = json.load(file)

# Iterate through each product category
for category, products in data.items():
    # Create a directory for the category
    category_dir = os.path.join('downloads', category)
    os.makedirs(category_dir, exist_ok=True)

    # Iterate through each product
    for product, links in products.items():
        # Create a directory for the product
        product_dir = fix_directory(os.path.join(category_dir, product))
        os.makedirs(product_dir, exist_ok=True)

        # Download each link for the product
        for link_name, link_url in links.items():
            # Remove spaces and create a filename
            filename = link_name.replace(' ', '_')
            # Download the file
            file_path = download_file(link_url, product_dir, filename)

            print(f"Downloaded: {file_path}")

print("Download completed!")
