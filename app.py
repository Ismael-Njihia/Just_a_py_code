from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random
from random_numbers import random_numbers
from last_names import all_names
from first_names import kenyan_first_names
from phone_numbers import random_number

# Set the path to the ChromeDriver executable
chromedriver_path = '/usr/bin/chromedriver'  # Replace with the actual path to chromedriver

# Create Chrome options
chrome_options = Options()
# Add any desired options
# chrome_options.add_argument('--headless')  # Run Chrome in headless mode (without GUI)

# Create a new instance of the Chrome driver with the specified options and service
driver = webdriver.Chrome(service=Service(chromedriver_path), options=chrome_options)

max_retries = 15000000000
retry_interval = 5

# Navigate to the login page
Tumechoka = 'https://tumechoka.net/'  # Replace with the actual login URL

# Function to fill and submit the form
def fill_and_submit_form():
    # Pick a random ID number
    IdNo = random.choice(random_numbers)

    # Phone number
    phone_No = random.choice(random_number)
    usePhone = '07' + str(phone_No)

    # Pick a random last name
    random_last_name = random.choice(all_names)

    # Pick a random first name
    random_first_name = random.choice(kenyan_first_names)

    try:
        driver.get(Tumechoka)

        # Wait until the page finishes loading
        wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        try:
            input_element = driver.find_element(By.NAME, 'id_number')
            input_element.send_keys(IdNo)
        except NoSuchElementException:
            print("Element not found")

        try:
            input_last_name = driver.find_element(By.NAME, 'last_name')
            input_last_name.send_keys(random_last_name)
        except NoSuchElementException:
            print("Element not last_name")

        try:
            input_first_name = driver.find_element(By.NAME, 'first_name')
            input_first_name.send_keys(random_first_name)
            time.sleep(2)
        except NoSuchElementException:
            print("Element not first_name")

        try:
            input_phone_number = driver.find_element(By.NAME, 'phone_number')
            input_phone_number.send_keys(usePhone)
            time.sleep(2)
        except NoSuchElementException:
            print("Element not number")

        try:
            input_county_name = driver.find_element(By.NAME, 'county')
            input_county_name.send_keys('Nairobi')
        except NoSuchElementException:
            print("Element not county")

        try:
            input_constituency_name = driver.find_element(By.NAME, 'constituency')
            input_constituency_name.send_keys('Kasarani')
        except NoSuchElementException:
            print("Element not constituency")

        try:
            input_ward_name = driver.find_element(By.NAME, 'ward')
            input_ward_name.send_keys('Mwiki')
        except NoSuchElementException:
            print("Element not ward")

        try:
            input_check_box = driver.find_element(By.NAME, 'status')
            input_check_box.click()
        except NoSuchElementException:
            print("Element not check box")

        # Execute JavaScript code to interact with the canvas element
        script = """
        var canvas = document.getElementById("sheet");
        var ctx = canvas.getContext("2d");

        // Set the stroke style and width for the signature
        ctx.strokeStyle = "red";
        ctx.lineWidth = 3;

        // Start drawing the signature
        ctx.beginPath();
        ctx.moveTo(50, 50);  // Set the starting point of the signature
        ctx.lineTo(200, 100);  // Draw a line
        ctx.lineTo(150, 200);  // Draw another line
        ctx.stroke();  // Finish drawing the signature
        """
        try:
            driver.execute_script(script)
        except NoSuchElementException:
            print("Element not script")

        try:
            confirm_btn = driver.find_element(By.ID, 'saveSign')
            confirm_btn.click()
            time.sleep(2)
        except NoSuchElementException:
            print("Element not savesign")

        try:
            submit_btn = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary.float-end')
            submit_btn.click()
            time.sleep(4)
        except NoSuchElementException:
            print("Element not submit")

        # Submit the form with the token value included
        form_element = driver.find_element(By.CSS_SELECTOR, 'form')
        driver.execute_script("arguments[0].setAttribute('target', '_self')", form_element)
        driver.execute_script(f"arguments[0].action = '{Tumechoka}/collect-signature'", form_element)
        driver.execute_script(f"arguments[0].enctype = 'multipart/form-data'", form_element)
        driver.execute_script(f"arguments[0].method = 'POST'", form_element)
        driver.execute_script(f"arguments[0].innerHTML += '<input type=\"hidden\" name=\"_token\" value=\"0MyObDpAOdKjkYW9ODuGPSOJzUrkhGXE48tDu0n4\">'", form_element)
        form_element.submit()

        time.sleep(2)
        print('Submitted ' + random_first_name)

        # Clear form fields for the next iteration
        input_element.clear()
        input_last_name.clear()
        input_first_name.clear()
        input_phone_number.clear()
        input_county_name.clear()
        input_constituency_name.clear()
        input_ward_name.clear()

    except Exception as e:
        print(f'Error: {str(e)}')

# Main execution loop
while True:
    try:
        fill_and_submit_form()
    except KeyboardInterrupt:
        # Exit the loop if Ctrl+C is pressed
        break
    except Exception:
        # Wait for the specified retry
        time.sleep(retry_interval)

# Quit the driver after the page finishes loading
driver.quit()
