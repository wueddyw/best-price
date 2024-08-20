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
    return {'title': title, 'price': price}

# Example usage
url = 'https://www.amazon.ca/Scotch-Gift-10-1m-Rolls-311X-OS-24/dp/B00ENFQFA2/ref=sr_1_5?crid=E2LXFJVL2C1M&dib=eyJ2IjoiMSJ9.jWSO6wYRlNPtvlTUSiX3c4ACJYhdzNRjul4lJgidReHDgpPB6tTxjyg9tJBV0sf4PmKEi61r4CkOoW9bOOQHzPrvw284_4Ad6tECJggK-1iQ0B9Y90Z_-qga1BU0KsRYnAUBP25QOW5z2JIRHUfTBARWlHSzGOD9xAvDP4HWRzR7aVaXfj7o9no1XoKpynX1jBvfuy0OWrPQnc1zsnefvxCcmQ4KxxfLnbm-IKpgLav_CSj39Slchu5-ZYgEHhHyvaYwf0sg6oPQpoccopTslt5Y6S3_Omf4MankiSh15og.HRVVxnlGCJkOFoph4HUCWzL-6awohrrWo6oQMezbuyc&dib_tag=se&keywords=tape&qid=1724121459&sprefix=tape%2Caps%2C233&sr=8-5'
data = scrape_amazon_selenium(url)
if data:
    print(data)
