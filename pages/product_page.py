from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class ProductPage(BasePage):
    def add_product_to_basket_with_qiuz(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()
        self.solve_quiz_and_get_code()

    def add_product_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket.click()

    def is_product_in_basket(self):
        self.is_product_name_in_basket()
        self.is_product_price_in_basket()

    def is_product_name_in_basket(self):
        try:
            product_name_title = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_TITLE)
            product_name_title_text = product_name_title.text
        except NoSuchElementException:
            product_name_title_text = '1'
        try:   
            product_name_added_to_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADDED_TO_BASKET)
            product_name_added_to_basket_text = product_name_added_to_basket.text
        except NoSuchElementException:
            product_name_added_to_basket_text = '2'
        assert product_name_title_text == product_name_added_to_basket_text, 'Added another product. Products name wrong'

    def is_product_price_in_basket(self):
        try:
            product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
            product_price_text = product_price.text
        except NoSuchElementException:
            product_price_text = '3'
        try:
            price_products_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCTS_IN_BASKET)
            price_products_in_basket_text = price_products_in_basket.text
        except NoSuchElementException:
            price_products_in_basket_text = '4'
        assert product_price_text == price_products_in_basket_text, 'Added another product. Products price wrong'
