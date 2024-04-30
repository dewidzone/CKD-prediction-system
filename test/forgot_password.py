
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TestForgotPassword(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000")

    def test_forgot_password(self):
        # Wait for the "Forgot Password?" link to be clickable
        try:
            forgot_password_link = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), 'Forgot Password?')]"))
            )
            # Click the "Forgot Password?" link
            forgot_password_link.click()

            # Fill out the email field
            email_input = self.driver.find_element(By.NAME, "email")
            email_input.send_keys("test@example.com")

            # Click the reset password button 
            reset_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Reset Password')]")
            reset_button.click()

            # Wait for a possible alert indicating successful password reset
            alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()

            # Check if the alert message is displayed
            self.assertEqual(alert_text, "check your email", "Forgot password was not handled correctly")

            print("\x1b[6;30;42m" + "Test passed. 'Check your email' message displayed." + "\x1b[0m")

        except TimeoutException:
            self.fail("No alert indicating successful password reset")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
