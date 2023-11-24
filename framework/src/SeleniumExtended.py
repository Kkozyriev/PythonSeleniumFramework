
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10
    def wait_and_input_text(self, locator, text,  timeout=None):
        timeout = timeout if timeout else self.default_timeout

        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)
    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        ).click()

    def wait_until_element_contains_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )