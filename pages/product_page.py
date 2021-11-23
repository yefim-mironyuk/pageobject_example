from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from .locators import ProductPageLocators, BasePageLocators
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def click_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        # BasePage.solve_quiz_and_get_code(self)

    def is_product_name_correct(self):
        message_name = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((
            ProductPageLocators.MESSAGE_NAME))).text
        real_name = self.browser.find_element(*ProductPageLocators.REAL_NAME).text
        assert message_name == real_name, "Real name and message name don't match"

    def is_price_correct(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, "Product price and basket price don't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message exists"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message didn't disappear"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
