# Import the necessary libraries
import mysql.connector

# Connect to the database
db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="pim_database"
)

# Get the user input for the new employee details
emp_id = input("Enter employee ID: ")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
email = input("Enter email: ")
phone = input("Enter phone number: ")
hire_date = input("Enter hire date (YYYY-MM-DD): ")
job_id = input("Enter job ID: ")
salary = input("Enter salary: ")
manager_id = input("Enter manager ID: ")
dept_id = input("Enter department ID: ")

# Create a cursor object to execute SQL queries
cursor = db.cursor()

# Define the SQL query to insert a new employee
sql = "INSERT INTO employees (employee_id, first_name, last_name, email, phone_number, hire_date, job_id, salary, manager_id, department_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
values = (emp_id, first_name, last_name, email, phone, hire_date, job_id, salary, manager_id, dept_id)

# Execute the SQL query to insert a new employee
cursor.execute(sql, values)

# Commit the changes to the database
db.commit()

# Print a message to confirm the new employee has been added
print(cursor.rowcount, "record inserted.")
