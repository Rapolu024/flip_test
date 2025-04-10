import requests
from bs4 import BeautifulSoup

def scrape_amazon(product_name):
    search_url = f"https://www.amazon.in/s?k={product_name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    response = requests.get(search_url, headers=headers)

    if response.status_code != 200:
        return {"error": "Failed to retrieve data from Amazon"}
    
    soup = BeautifulSoup(response.text, "html.parser")
    product = soup.find("div", {"class": "s-main-slot"}).find("div")

    try:
        title = product.find("span", {"class": "a-text-normal"}).text.strip()
        price = product.find("span", {"class": "a-price-whole"}).text.strip()
        rating = product.find("span", {"class": "a-icon-alt"}).text.strip()
        reviews = product.find("span", {"class": "a-size-base"}).text.strip()
        url = "https://www.amazon.in" + product.find("a", {"class": "a-link-normal"})["href"]
        
        return {"name": title, "price": price, "rating": rating, "reviews": reviews, "url": url}
    except AttributeError:
        return {"error": "Product data not found"}

def scrape_flipkart(product_name):
    search_url = f"https://www.flipkart.com/search?q={product_name}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    response = requests.get(search_url, headers=headers)

    if response.status_code != 200:
        return {"error": "Failed to retrieve data from Flipkart"}
    
    soup = BeautifulSoup(response.text, "html.parser")
    product = soup.find("div", {"class": "_1AtVbE"}).find("div", {"class": "_2kHMtA"})
    
    try:
        title = product.find("a", {"class": "IRpwTa"}).text.strip()
        price = product.find("div", {"class": "_30jeq3"}).text.strip()
        rating = product.find("div", {"class": "_3LWZlK"}).text.strip()
        reviews = product.find("span", {"class": "_2_R_DZ"}).text.strip()
        url = "https://www.flipkart.com" + product.find("a", {"class": "IRpwTa"})["href"]
        
        return {"name": title, "price": price, "rating": rating, "reviews": reviews, "url": url}
    except AttributeError:
        return {"error": "Product data not found"}
