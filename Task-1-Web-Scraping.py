# Task 1 - Web Scraping using BeautifulSoup

# Import Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send Request to Website
response = requests.get(url)

# Parse HTML Content
soup = BeautifulSoup(response.text, "html.parser")

# Find All Book Containers
books = soup.find_all("article", class_="product_pod")

# Create Empty Lists
book_names = []
prices = []
ratings = []

# Extract Data
for book in books:
    
    # Book Name
    name = book.h3.a["title"]
    book_names.append(name)
    
    # Price
    price = book.find("p", class_="price_color").text
    prices.append(price)
    
    # Rating
    rating = book.p["class"][1]
    ratings.append(rating)

# Create DataFrame
data = pd.DataFrame({
    "Book Name": book_names,
    "Price": prices,
    "Rating": ratings
})

# Display Data
print(data)

# Save Dataset to CSV
data.to_csv("books_data.csv", index=False)

print("\nData saved successfully as books_data.csv")
