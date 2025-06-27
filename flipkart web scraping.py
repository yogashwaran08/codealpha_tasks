import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define the search URL
query = "laptop"
url = f"https://www.flipkart.com/search?q={query}"

# Step 2: Set headers to mimic a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

# Step 3: Send the HTTP request
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Step 4: Extract product containers
product_cards = soup.find_all("div", class_="_1AtVbE")  # generic container class

# Step 5: Parse titles and prices
products = []

for card in product_cards:
    title_tag = card.find("div", class_="_4rR01T")  # product title class
    price_tag = card.find("div", class_="_30jeq3")  # price class

    if title_tag and price_tag:
        title = title_tag.get_text(strip=True)
        price = price_tag.get_text(strip=True)
        products.append({"Title": title, "Price": price})

# Step 6: Save to CSV
df = pd.DataFrame(products)
df.to_csv("flipkart_laptops.csv", index=False)

# Step 7: Print sample
print(" Scraping successful! Sample data:")
print(df.head())
