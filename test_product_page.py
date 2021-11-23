from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
import pytest

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket()
    page.is_product_name_correct()
    page.is_price_correct()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.negative_test
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket()
    page.should_not_be_success_message()


@pytest.mark.negative_test
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.negative_test
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket()
    page.should_disappear_of_success_message()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
