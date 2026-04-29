# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# options = webdriver.ChromeOptions()

# # options.add_argument("--headless=new")


# driver = webdriver.Chrome(
#     options=options,
# )




# driver.get("https://www.scrapingcourse.com/login")

# # retrieve the form elements
# email_input = driver.find_element(By.ID, "email")
# password_input = driver.find_element(By.ID, "password")
# submit_button = driver.find_element(By.ID, "submit-button")



# element = WebDriverWait(driver, 5).until(
#     EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".form-group"))
# )
# # filling out the form elements
# email_input.send_keys("admin@example.com")

# password_input.send_keys("password")

# # submit the form and log in
# submit_button.click()

# driver.save_screenshot("form_filled.jpg")


import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def human_type(element, text, min_delay=0.1, max_delay=0.3):
    """Types text character-by-character with random delays."""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(min_delay, max_delay))

# 1. Setup Driver
options = webdriver.ChromeOptions()
# options.add_argument("--headless=new") # Uncomment if running in headless mode
driver = webdriver.Chrome(options=options)

driver.get("https://www.scrapingcourse.com/login")

# 2. Use WebDriverWait to ensure the form is loaded before interacting
# This waits up to 10 seconds for the form to be visible
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID, "email")))

# 3. Retrieve form elements
email_input = driver.find_element(By.ID, "email")
password_input = driver.find_element(By.ID, "password")
submit_button = driver.find_element(By.ID, "submit-button")

# 4. Fill form using human-like typing
human_type(email_input, "admin@example.com")
human_type(password_input, "password")

# 5. Submit the form
submit_button.click()

# 6. Save a screenshot
# Small wait to allow the page to navigate/react before taking the screenshot
time.sleep(2)
driver.save_screenshot("form_filled.jpg")

driver.quit()