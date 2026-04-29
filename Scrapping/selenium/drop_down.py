from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")

#  Define the wait instance
wait = WebDriverWait(driver, 5)

#  Use the wait to find the element
# This will now wait up to 5 seconds for the element to be present
dropdown_element = wait.until(
    EC.presence_of_element_located((By.ID, "dropdown"))
)

#  Create a Select object and interact
select = Select(dropdown_element)
select.select_by_visible_text("Option 2")

print(f"Selected option is: {select.first_selected_option.text}")

driver.quit()