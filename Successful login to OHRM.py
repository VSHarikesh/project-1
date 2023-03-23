from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Define the URL and credentials for the login page
url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
username = 'admin'
password = 'admin123'

# Create a new instance of the Firefox browser
browser = webdriver.Chrome()

# Navigate to the login page
browser.get(url)

# Find the username and password fields and enter the credentials
username_field = browser.find_element_by_name('Username')
username_field.send_keys(username)
password_field = browser.find_element_by_name('Password')
password_field.send_keys(password)

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for the dashboard page to load
browser.implicitly_wait(10)

# Close the browser
browser.quit()