import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_countdown_price():
    url = "https://www.woolworths.co.nz/shop/productdetails?stockcode=135344&name=fresh-vegetable-carrots"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(30)  # Allow time for JavaScript to load
    
    try:
        price_element = driver.find_element(By.CLASS_NAME, "price")
        price = price_element.text.replace("$", "")
        return float(price)
    except:
        return None
    finally:
        driver.quit()

def get_new_world_price():
    url = "https://www.newworld.co.nz/shop/product/5039965_kgm_000nw?name=-carrots"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(30)  # Allow time for JavaScript to load
    
    try:
        price_element = driver.find_element(By.CLASS_NAME, "currency-value")
        price = price_element.text.replace("$", "")
        return float(price)
    except:
        return None
    finally:
        driver.quit()

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

