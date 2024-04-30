import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException

class TestRegisterAndLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000")

    def tearDown(self):
        self.driver.quit()

    def test_login_with_already_use_email(self):
        # Click the SignUp button
        Sign_up_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'SignUp')]")
        Sign_up_button.click()

        # Fill the email and password fields with a Already used email address
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")
        email_input.send_keys("test24@example.com")

        # Introduce a delay
        time.sleep(1)

        password_input.send_keys("password123@@")

        # Click the SignUp button
        submit_button = self.driver.find_element(By.CLASS_NAME, "btn.btn-primary.btn-block")
        
        # Introduce a delay
        time.sleep(1)

        submit_button.click()

        try:
            # Wait for a possible alert indicating invalid credential
            alert = WebDriverWait(self.driver, 40).until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()

            # Introduce a delay
            time.sleep(2)

            if "auth/email-already-in-use" in alert_text:
                print("\x1b[6;30;42m" + "Test passed. 'auth/email-already-in-use' message displayed." + "\x1b[0m")
            else:
                self.fail("SignUp with already used email was not handled correctly")

        except TimeoutException:
            # If no alert is present, fail the test
            self.fail("No alert indicating invalid credentials")

if __name__ == "__main__":
    unittest.main()
