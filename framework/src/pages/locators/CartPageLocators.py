from selenium.webdriver.common.by import By


class CartPageLocators:

    PRODUCT_NAMES_IN_CART = (By.CSS_SELECTOR, 'a.wc-block-components-product-name')
    ADD_A_COUPON_BTN = (By.CSS_SELECTOR, '.wc-block-components-totals-coupon-link')
    COUPON_FIELD = (By.ID, 'wc-block-components-totals-coupon__input-0')
    APPLY_COUPON_BTN = (By.CSS_SELECTOR, '.wc-block-components-totals-coupon__button')
    COUPON_APPLIED_PUSH_UP = (By.CSS_SELECTOR, 'div.wc-block-components-notice-banner__content')