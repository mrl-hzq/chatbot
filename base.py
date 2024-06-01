from selenium import webdriver
from selenium.webdriver.common.service import Service
import time

# Path to your Chrome WebDriver
# webdriver_path = ''
service = Service(executable_path="chromedriver.exe")

# Initialize Chrome WebDriver with the path to the executable
driver = webdriver.Chrome(service=service)

# Open Google's homepage
driver.get("https://www.google.com")
time.sleep(10)  # Wait for the page to load

# Find the search input field
search_input = driver.find_element_by_name('q')

# Send a test search query
search_input.send_keys('Test search query')
search_input.send_keys(Keys.RETURN)

# Close the browser window
# driver.quit()
	