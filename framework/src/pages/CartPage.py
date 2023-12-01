from framework.src.pages.locators.CartPageLocators import CartPageLocators
from framework.src.SeleniumExtended import  SeleniumExtended

class CartPage(CartPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_cart_page(self):
        pass

    def get_all_product_names_in_cart(self):
        product_name_elements = self.sl.wait_and_get_elements(self.PRODUCT_NAMES_IN_CART)
        product_names = [i.text for i in product_name_elements]
        return product_names

    def click_add_a_coupon(self):
        self.sl.wait_and_click(self.ADD_A_COUPON_BTN)

    def input_coupon(self, coupon_code):
        self.sl.wait_and_input_text(self.COUPON_FIELD, coupon_code)

    def click_apply_coupon(self):
        self.sl.wait_and_click(self.APPLY_COUPON_BTN)

    def get_displayed_message(self):
        self.sl.wait_until_element_is_visible(self.COUPON_APPLIED_PUSH_UP)

    def apply_coupon(self, coupon_code):
        self.click_add_a_coupon()
        self.input_coupon(coupon_code)
        self.click_apply_coupon()
        self.get_displayed_message()
