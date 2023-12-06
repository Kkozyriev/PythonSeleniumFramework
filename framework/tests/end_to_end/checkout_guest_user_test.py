import time
import pytest
from framework.src.pages.HomePage import HomePage
from framework.src.pages.Header import Header
from framework.src.pages.CartPage import CartPage
from framework.src.pages.CheckoutPage import CheckoutPage
from framework.src.pages.OrderConfirmationPage import OrderConfirmationPage
from framework.src.configs.GeneralConfigs import GeneralConfigs
from framework.src.configs.TestDataConfigs import TestDataConfigs
from framework.src.helpers.DatabaseHelpers import get_order_from_db_by_order_no


@pytest.mark.usefixtures('init_driver')
class TestCheckoutGuestUser:
    @pytest.mark.tcid33
    def test_checkout_guest_user(self):

        home_p = HomePage(self.driver)
        header = Header(self.driver)
        cart_p = CartPage(self.driver)
        checkout_p = CheckoutPage(self.driver)
        order_confirmation_p = OrderConfirmationPage(self.driver)

        # go to home page
        home_p.go_to_home_page()

        # add 1 item to cart
        home_p.click_first_add_to_cart_button()

        # make sure the cart is updated before going to cart
        header.wait_until_cart_item_count(1)

        # go to cart
        header.click_on_cart_on_right_header()
        product_names = cart_p.get_all_product_names_in_cart()
        assert len(product_names) == 1, f"Expected 1 item in cart but found {len(product_names)}"

        # apply free coupon
        coupon_code = TestDataConfigs.FREE_COUPON
        cart_p.apply_coupon(coupon_code)

        # click on checkout
        cart_p.click_on_proceed_to_checkout()

        # fill in form
        checkout_p.fill_in_billing_info()

        # click on place order
        checkout_p.click_place_order()

        # verify order is received
        order_confirmation_p.verify_order_confirmation_page_loaded()

        # verify order is recorded in db (via SQL or via API)
        order_num = order_confirmation_p.get_order_number()
        print('*********')
        print(order_num)
        print('*********')

        db_order = get_order_from_db_by_order_no(order_num)
        assert db_order, (f"After creating order with FE, not found in DB."
                          f"Order no:{order_num}")

        print("")
        print("******")
        print("PASS")
        print("******")