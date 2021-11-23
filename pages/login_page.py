from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.endswith('login/'), 'Wrong url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password, browser):
        emailstr = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((LoginPageLocators.REGISTER_BLANK_EMAIL)))
        emailstr.send_keys(email)
        passwordstr = self.browser.find_element(*LoginPageLocators.REGISTER_BLANK_PASSWORD)
        passwordstr.send_keys(password)
        passwordconf = self.browser.find_element(*LoginPageLocators.REGISTER_BLANK_CONFIRM_PASSWORD)
        passwordconf.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()
