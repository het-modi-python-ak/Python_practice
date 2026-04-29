
# from selenium import webdriver
 
# # initialize an instance of the chrome driver (browser)
# driver = webdriver.Chrome()

# # visit your target site
# driver.get("https://www.geeksforgeeks.org/python/selenium-python-tutorial/")

# print(driver.page_source)

# # release the resources allocated by Selenium and shut down the browser
# driver.quit()






from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()

options.add_argument("--headless=new")


driver = webdriver.Chrome(
    options=options,
)


driver.get("https://www.scrapingcourse.com/ecommerce")


products = driver.find_elements(By.CSS_SELECTOR, ".product")

extracted_products = []

# loop  the product containers
for product in products:

    # extract the elements into a dictionary using the CSS selector
    product_data = {
        "name": product.find_element(By.CSS_SELECTOR, ".product-name").text,
        "price": product.find_element(By.CSS_SELECTOR, ".price").text,
        "URL": product.find_element(
            By.CSS_SELECTOR, ".woocommerce-LoopProduct-link"
        ).get_attribute("href"),
        "image": product.find_element(By.CSS_SELECTOR, ".product-image").get_attribute(
            "src"
        ),
    }


    extracted_products.append(product_data)




# print the extracted data
print(extracted_products)




#saving data in the csv
import csv

csv_file = "products.csv"

# write the extracted data to the CSV file
with open(csv_file, mode="w", newline="", encoding="utf-8") as file:
    # write the headers
    writer = csv.DictWriter(file, fieldnames=["URL", "image", "name", "price"])
    writer.writeheader()
    # write the rows
    writer.writerows(extracted_products)

# confirm that the data has been written to the CSV file
print(f"Data has been written to {csv_file}")









#click butoon
driver.get("https://www.scrapingcourse.com/javascript-rendering")

# get the brand name element
brand_name = driver.find_element(By.CSS_SELECTOR, ".brand-name")

# perform a click action
brand_name.click()

# screenshot the result page
driver.save_screenshot("homepage-screenshot.png")

#screens shots 



prodcut = driver.find_element(By.CSS_SELECTOR, ".product-image")
product.click()

driver.save_screenshot("albenia")







from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def get_data():
    return extracted_products






driver.quit()
