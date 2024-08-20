from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def scrape_amazon_selenium(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.get(url)
    
    try:
        title = driver.find_element(By.ID, 'productTitle').text
    except:
        title = 'Title not available'
        
    try:
        # Extract the price parts
        price_symbol = driver.find_element(By.CLASS_NAME, 'a-price-symbol').text
        price_whole = driver.find_element(By.CLASS_NAME, 'a-price-whole').text
        price_fraction = driver.find_element(By.CLASS_NAME, 'a-price-fraction').text
        
        # Combine the parts to form the full price
        price = f"{price_symbol}{price_whole}.{price_fraction}"
    except:
        price = 'Price not available'
    
    driver.quit()
    # Print the scraped data
    print(f"Title: {title}")
    print(f"Price: {price}")
    return {'title': title, 'price': price}
