from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the webdriver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the orangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/")
wait = WebDriverWait(driver, 5)

# Enter invalid login credentials
username = wait.until(EC.visibility_of_element_located((By.ID, "txtUsername")))
username.clear()
username.send_keys("invalid_username")

password = wait.until(EC.visibility_of_element_located((By.ID, "txtPassword")))
password.clear()
password.send_keys("invalid_password")

# Click the login button
login_button = wait.until(EC.visibility_of_element_located((By.ID, "btnLogin")))
login_button.click()

# Verify that the login failed
error_message = wait.until(EC.visibility_of_element_located((By.ID, "spanMessage")))
assert error_message.text == "Invalid credentials"
print("Invalid login test passed!")

# Close the webdriver
driver.quit()