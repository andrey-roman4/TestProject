from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('offer_number', ['0', '1', '2', '3', '4', '5', '6', pytest.param('7', marks=pytest.mark.xfail), '8', '9'])
def test_guest_can_add_product_to_basket(browser, offer_number):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket_with_qiuz()
    page.is_product_name_in_basket()
    page.is_product_price_in_basket()

@pytest.mark.parametrize('offer_number', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
def test_is_product_name_in_basket(browser, offer_number):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_number}'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.is_product_name_in_basket()

def test_is_product_price_in_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.is_product_price_in_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_should_not_be_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_should_be_disappeared_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_disappeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()