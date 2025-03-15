import requests
from bs4 import BeautifulSoup

def get_countdown_price():
    url = "https://www.countdown.co.nz/shop/searchproducts?search=carrots"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        product = soup.find("div", class_="product-tile")
        if product:
            price = product.find("span", class_="value")
            return float(price.text) if price else None
    return None

def get_new_world_price():
    url = "https://www.newworld.co.nz/shop/search?q=carrots"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        product = soup.find("div", class_="product-tile")
        if product:
            price = product.find("span", class_="currency-value")
            return float(price.text) if price else None
    return None

def compare_prices():
    countdown_price = get_countdown_price()
    new_world_price = get_new_world_price()
    
    print("Carrot Price Comparison:")
    print(f"Countdown: ${countdown_price if countdown_price else 'Not Found'}")
    print(f"New World: ${new_world_price if new_world_price else 'Not Found'}")
    
    if countdown_price and new_world_price:
        if countdown_price < new_world_price:
            print("Countdown has cheaper carrots!")
        elif new_world_price < countdown_price:
            print("New World has cheaper carrots!")
        else:
            print("Both stores have the same price for carrots.")

if __name__ == "__main__":
    compare_prices()
