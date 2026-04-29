import time

from selenium import webdriver

from selenium.webdriver.common.by import By



# instantiate a Chrome options object

options = webdriver.ChromeOptions()



# set the options to use Chrome in headless mode

options.add_argument("--headless=new")



# initialize an instance of the Chrome driver 

driver = webdriver.Chrome(

    options=options,

)





driver.get("https://www.scrapingcourse.com/infinite-scrolling")





last_height = driver.execute_script("return document.body.scrollHeight")

while True:

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    time.sleep(5)


    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
      
        break

    last_height = new_height


# extract all product containers

products = driver.find_elements(By.CSS_SELECTOR, ".product-item")




extracted_products = []


#
for product in products:

    product_data = {

        "Name": product.find_element(By.CSS_SELECTOR, ".product-name").text,

        "Price": product.find_element(By.CSS_SELECTOR, ".product-price").text,

    }

    extracted_products.append(product_data)


# output the data

print(extracted_products)


# release the resources allocated by Selenium and shut down the browser

driver.quit()
