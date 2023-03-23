from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# specify the path to the chromedriver executable
driver_path = '/path/to/chromedriver'

# create a new Chrome browser instance
browser = webdriver.Chrome(executable_path=driver_path)

# navigate to the OrangeHRM login page
browser.get('https://yourcompany.orangehrm.com/auth/login')

# enter the login credentials and submit the form
username = browser.find_element_by_id('txtUsername')
username.send_keys('your_username')
password = browser.find_element_by_id('txtPassword')
password.send_keys('your_password')
password.send_keys(Keys.RETURN)

# navigate to the PIM module and search for the employee
browser.get('https://yourcompany.orangehrm.com/pim/viewEmployeeList')
search_box = browser.find_element_by_id('empsearch_employee_name_empName')
search_box.send_keys('John Doe')  # replace with the name of the employee you want to edit
search_box.send_keys(Keys.RETURN)

# click on the employee record to open the editing form
employee_record = browser.find_element_by_xpath("//a[contains(text(),'John Doe')]")
employee_record.click()

# edit the employee details
first_name = browser.find_element_by_id('firstName')
first_name.clear()  # clear the existing first name
first_name.send_keys('John')  # enter the new first name
last_name = browser.find_element_by_id('lastName')
last_name.clear()  # clear the existing last name
last_name.send_keys('Smith')  # enter the new last name
# repeat the above steps for any other fields you want to edit

# submit the changes
save_button = browser.find_element_by_id('btnSave')
save_button.click()

# close the browser
browser.quit()
