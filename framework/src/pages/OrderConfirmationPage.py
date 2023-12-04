
from framework.src.SeleniumExtended import SeleniumExtended
from framework.src.pages.locators.OrderConfirmationPageLocators import OrderConfirmationPageLocators


class OrderConfirmationPage(OrderConfirmationPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_order_confirmation_page_loaded(self):
        self.sl.wait_until_element_is_visible(self.PAGE_MAIN_HEADER)

    def get_order_number(self):
        return self.sl.wait_and_get_text(self.ORDER_NUMBER)