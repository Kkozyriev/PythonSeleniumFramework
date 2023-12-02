
from selenium.webdriver.common.by import By


class CheckoutPageLocators:
    BILLING_EMAIL_ADDRESS = (By.ID, 'email')
    BILLING_FIRST_NAME_FIELD = (By.ID, 'billing-first_name')
    BILLING_LAST_NAME_FIELD = (By.ID, 'billing-last_name')
    BILLING_ADDRESS_1_FIELD = (By.ID, 'billing-address_1')
    BILLING_ADDRESS_2_FIELD = (By.ID, 'billing-address_2')  # optional
    BILLING_COUNTRY = (By.ID, 'components-form-token-input-0')
    BILLING_COUNTRY_POLAND = (By.ID, 'components-form-token-suggestions-0-175')
    BILLING_POSTCODE = (By.ID, 'billing-postcode')
    BILLING_CITY = (By.ID, 'billing-city')
    BILLING_PHONE = (By.ID, 'billing-phone')

    PLACE_ORDER_BTN = (By.CSS_SELECTOR, 'button.wc-block-components-checkout-place-order-button')

