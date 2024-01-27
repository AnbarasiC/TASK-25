'''Using Python Selenium, Explicit Wait, Expected Conditions and
Chrome Webdriver kindly do the following task mentioned below:

1) Go to https://www.imdb.com/search/name/
2) Fill the data given in the Input Boxes, Select Boxes and Drop Drown menu
on the webpage and do a search.
3) Do not use the sleep() method for the task.'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

# Create a new Chrome WebDriver instance
driver = webdriver.Chrome(options=chrome_options)

# Go to IMDb search page
driver.get("https://www.imdb.com/search/name/")

# Define an explicit wait with a timeout of 10 seconds
wait = WebDriverWait(driver, 10)

expand_l = wait.until(EC.presence_of_element_located((By.XPATH,"//span[normalize-space()='Expand all']")))
expand_l.click()

# Fill the input boxes
name_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class='ipc-textfield__input' and @aria-label='Name']")))
name_input.clear()
name_input.send_keys("Brendan Fraser")

birth_date_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='birth-date-start-input']")))
birth_date_input.clear()
birth_date_input.send_keys("03-12-1968")

birth_day_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class='ipc-textfield__input' and @aria-label='Enter birthday']")))
birth_day_input.clear()
birth_day_input.send_keys("12-03")

# Select Boxes
awards_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='awardsAccordion']//button[2]")))
awards_button.click()

page_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='pageTopicsAccordion']//button[1]")))
page_button.click()

# Selecting Drop Drown menu
birth_place_select = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='within-topic-dropdown-id']")))
birth_place_select.click()
birth_place_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='BIRTH_PLACE']")))
birth_place_option.click()

# Select gender boxes
gender_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='genderIdentityAccordion']//button[1]")))
gender_button.click()

#Perform search
search_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='See results']")))
search_button.click()

# Print the search results title
print(driver.title)

# Close the browser window
driver.quit()