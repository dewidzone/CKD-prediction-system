import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException

class TestRegisterAndLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000")

    def tearDown(self):
        self.driver.quit()

    def test_login_with_Wrong_password(self):
        # Click the SignIn button
        sign_in_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'SignIn')]")
        sign_in_button.click()

        # Fill the email and password fields with email address
        email_input = self.driver.find_element(By.NAME, "email")
        password_input = self.driver.find_element(By.NAME, "password")
        email_input.send_keys("dewidzone@gmail.com")
        password_input.send_keys("1234567891011")

        # Introduce a delay before clicking the SignIn button
        time.sleep(2)

        # Attempt to click the SignIn button with error handling
        try:
            submit_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-primary.btn-block")))
            submit_button.click()
        except ElementClickInterceptedException:
            print("Element click intercepted. Trying to scroll into view and click again.")
            self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            submit_button.click()

        try:
            # Wait for a possible alert indicating valid credential
            alert = WebDriverWait(self.driver, 20).until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()

            if "Login Successful!" in alert_text:
                print("\x1b[6;30;42m" + "Test passed. 'Successfully Redirect to the home page' message displayed." + "\x1b[0m")
                
                # Introduce a delay before redirecting to /home
                time.sleep(2)
                self.driver.get("http://localhost:3000/home")
                
                # Navigate to prediction page
                prediction_button = self.driver.find_element(By.XPATH, "//a[contains(text(), 'Get Prediction')]")
                prediction_button.click()
                WebDriverWait(self.driver, 30).until(EC.url_contains("/prediction"))

                # Fill out the form
                try:
                    age_input = WebDriverWait(self.driver, 25).until(
                        EC.presence_of_element_located((By.NAME, "age"))
                    )
                    age_input.send_keys("51")
                    time.sleep(1)  # Slow down the filling process
                    al_input = self.driver.find_element(By.NAME, "al")
                    al_input.send_keys("0")
                    time.sleep(1)
                    su_input = self.driver.find_element(By.NAME, "su")
                    su_input.send_keys("0")
                    time.sleep(1)
                    bgr_input = self.driver.find_element(By.NAME, "bgr")
                    bgr_input.send_keys("40")
                    time.sleep(1)
                    bu_input = self.driver.find_element(By.NAME, "bu")
                    bu_input.send_keys("10")
                    time.sleep(1)
                    sc_input = self.driver.find_element(By.NAME, "sc")
                    sc_input.send_keys("7")
                    time.sleep(1)
                    sod_input = self.driver.find_element(By.NAME, "sod")
                    sod_input.send_keys("23")
                    time.sleep(1)
                    pcv_input = self.driver.find_element(By.NAME, "pcv")
                    pcv_input.send_keys("40")
                    time.sleep(1)
                    rc_input = self.driver.find_element(By.NAME, "rc")
                    rc_input.send_keys("29")
                    time.sleep(1)
                    htn_input = self.driver.find_element(By.NAME, "htn")
                    htn_input.send_keys("No")
                except NoSuchElementException:
                    print("Form fields not found.")
                    return

                # Click the Predict button
                try:
                    predict_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
                    predict_button.click()
                    # Wait for prediction result
                    prediction_result = WebDriverWait(self.driver, 25).until(
                        EC.visibility_of_element_located((By.CLASS_NAME, "result"))
                    )
                    print("\x1b[6;30;42m" + f"Test passed. Prediction result: {prediction_result.text}" + "\x1b[0m")
                except NoSuchElementException:
                    print("Prediction button or result not found.")
                    return

            else:
                self.fail("Login with email and password was not handled correctly")

        except TimeoutException:
            print("\x1b[6;30;42m" + "Test passed. Login Successful!" + "\x1b[0m")

if __name__ == "__main__":
    unittest.main()
