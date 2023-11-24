
from framework.src.pages.locators import MyAccountSignedOutLocator
from framework.src.SeleniumExtended import SeleniumExtended
from framework.src.helpers.config_helpers import get_base_url


class MyAccountSignedOut(MyAccountSignedOutLocator):
    endpoint ='/my-account'
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        self.sl.wait_and_click(self.LOGIN_BTN)

