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
        product_name_title = self.get_text(*ProductPageLocators.PRODUCT_NAME_TITLE)
        product_name_added_to_basket = self.get_text(*ProductPageLocators.PRODUCT_NAME_ADDED_TO_BASKET)
        assert product_name_title == product_name_added_to_basket, 'Added another product. Products name wrong'

    def is_product_price_in_basket(self):
        product_price = self.get_text(*ProductPageLocators.PRODUCT_PRICE)
        price_products_in_basket = self.get_text(*ProductPageLocators.PRICE_PRODUCTS_IN_BASKET)
        assert product_price == price_products_in_basket, 'Added another product. Products price wrong'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCES_MESSAGE), \
       "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCES_MESSAGE), \
       "Success message is not disappeared, but should be"