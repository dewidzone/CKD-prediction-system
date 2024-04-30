import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException

class TestRegisterAndLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000")

    def tearDown(self):
        self.driver.quit()

    def test_signup(self):
        # Click the SignUp button
        sign_up_btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'SignUp')]")
        sign_up_btn.click()

        # Fill the email and password fields with a new email address
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")
        email_input.send_keys("test36@example.com")
        password_input.send_keys("password123@@")

        # Introduce a delay
        time.sleep(1)

        # Click the SignUp button
        submit_button = self.driver.find_element(By.CLASS_NAME, "btn.btn-primary.btn-block")
        submit_button.click()

        try:
            # Wait for the alert to appear
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())

            # Switch to the alert and accept it
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            alert.accept()

            # Assert the alert message
            self.assertEqual(alert_text, "Registration Successful!")

            # Introduce a delay
            time.sleep(2)

            # Wait for navigation to home page
            WebDriverWait(self.driver, 20).until(EC.url_contains("/home"))

            # Assert that we are redirected to the home page
            self.assertIn("/home", self.driver.current_url)
            print("\x1b[6;30;42m" + "Test passed. Redirected to home page." + "\x1b[0m")

        except NoAlertPresentException:
            print("\x1b[1;31;40m" + "No alert was present." + "\x1b[0m")
            self.fail("Alert was expected but not found.")

if __name__ == "__main__":
    unittest.main()
