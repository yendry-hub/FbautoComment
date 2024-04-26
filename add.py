from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
import time

def interact_with_page(driver):
    # Your code to interact with the page goes here
    try:
        # Find the element on the page
        element = driver.find_element_by_xpath("//*[contains(text(), 'Just now')]")
        
        # Click on the element if found
        element.click()
        
        # If successful, return True to indicate success
        return True
        
    except NoSuchElementException:
        # If element is not found, return False to indicate failure
        return False

def main():
    url = "https://example.com"  # Replace with your URL
    email = "your_email@example.com"  # Replace with your email
    password = "your_password"  # Replace with your password

    driver = Chrome()
    try:
        # Login to Facebook or perform any necessary actions
        # Navigate to the URL
        driver.get(url)
        
        # Wait for the alert to be present
        WebDriverWait(driver, 10).until(EC.alert_is_present())

        # Switch to the alert and accept it (click "Allow")
        alert = driver.switch_to.alert
        alert.accept()

        # Interact with the page
        success = interact_with_page(driver)

        if not success:
            # If interaction failed, refresh the page
            driver.refresh()
            time.sleep(2)  # Wait for the page to refresh
            
            # Call the main function again to restart the process
            main()
        
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()

# Call the main function to start the script
if __name__ == "__main__":
    main()
