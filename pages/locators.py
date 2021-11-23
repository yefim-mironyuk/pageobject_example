from selenium.webdriver.common.by import By


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    MESSAGE_NAME = (By.CSS_SELECTOR, ".alertinner strong")
    REAL_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
