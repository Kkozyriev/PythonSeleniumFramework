from framework.src.SeleniumExtended import SeleniumExtended
from framework.src.pages.locators.CheckoutPageLocators import CheckoutPageLocators
from framework.src.helpers.GenericHelpers import generate_random_email_and_password


class CheckoutPage(CheckoutPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(driver)

    def input_billing_email(self, email=None):
        if not email:
            rand_email = generate_random_email_and_password()
            email = rand_email['email']
        self.sl.wait_and_input_text(self.BILLING_EMAIL_ADDRESS, email)

    #

    def input_billing_first_name(self, first_name=None):
        first_name = first_name if first_name else "AutomationFirstname"
        self.sl.wait_and_input_text(self.BILLING_FIRST_NAME_FIELD, first_name)

    def input_billing_last_name(self, last_name=None):
        last_name = last_name if last_name else "AutomationLastname"
        self.sl.wait_and_input_text(self.BILLING_LAST_NAME_FIELD, last_name)

    def input_billing_street_address_1(self, address1=None):
        address1 = address1 if address1 else "123 Main st."
        self.sl.wait_and_input_text(self.BILLING_ADDRESS_1_FIELD, address1)

    def input_billing_postcode(self, postcode=None):
        postcode = postcode if postcode else "02-123"
        self.sl.wait_and_input_text(self.BILLING_POSTCODE, postcode)

    def input_billing_city(self, city=None):
        city = city if city else "Warsaw"
        self.sl.wait_and_input_text(self.BILLING_CITY, city)

    def input_billing_phone_number(self, phnum=None):
        phnum = phnum if phnum else '4151111111'

    def fill_in_billing_info(self, f_name=None, l_name=None, street1=None, city=None, postcode=None, phone_number=None, email=None):
        self.input_billing_email(email=email)
        self.input_billing_first_name(first_name=f_name)
        self.input_billing_last_name(last_name=l_name)
        self.input_billing_street_address_1(address1=street1)
        self.input_billing_city(city=city)
        self.input_billing_postcode(postcode=postcode)
        self.input_billing_phone_number(phnum=phone_number)

    def click_place_order(self):
        self.sl.wait_and_click(self.PLACE_ORDER_BTN)

