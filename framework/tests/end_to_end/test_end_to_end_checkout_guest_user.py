import time
import pytest
from framework.src.pages.HomePage import HomePage
from framework.src.pages.Header import Header

@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuestUser:
    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):

        home_p = HomePage(self.driver)
        header = Header(self.driver)

        # go to home page
        home_p.go_to_home_page()

        # add 1 item to cart
        home_p.click_first_add_to_cart_button()

        #make sure the cart is updated before going to cart
        header.wait_until_cart_item_count(1)
        # go to cart
        header.click_on_cart_on_right_header()
        time.sleep(6)
        #apply free coupon

        #select gree shipping

        #click on checkout

        #fill in form

        #click on place order

        #verify order is received

        #verife order is recorderd in db (vuia SQL or via API)