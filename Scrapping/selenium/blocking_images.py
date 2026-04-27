# import the required libraries

from selenium import webdriver

from selenium.webdriver.chrome.options import Options



# run Chrome in headless mode

options = Options()





# disable Blink to disallow images

options.add_argument("--blink-settings=imagesEnabled=false")



# set the options to use Chrome in headless mode

# options.add_argument("--headless=new")



# start a driver instance

driver = webdriver.Chrome(options=options)



# open the target website

driver.get("https://www.scrapingcourse.com/ecommerce")



# take a screenshot of the page

driver.save_screenshot("screenshot_with-no-image.png")



# release the resources allocated by Selenium and shut down the browser

driver.quit()
