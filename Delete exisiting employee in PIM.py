import requests

# Set the API endpoint for deleting an employee
endpoint = "https://your-portal-url/pim/v1/employees/{employee_id}"

# Set the ID of the employee you want to delete
employee_id = 1234

# Set the authentication credentials for your portal
auth = ('your_username', 'your_password')

# Send the HTTP DELETE request to delete the employee
response = requests.delete(endpoint.format(employee_id=employee_id), auth=auth)

# Check the response status code to ensure the employee was successfully deleted
if response.status_code == 204:
    print(f"Employee with ID {employee_id} successfully deleted!")
else:
    print(f"Error deleting employee with ID {employee_id}: {response.status_code} {response.text}")
