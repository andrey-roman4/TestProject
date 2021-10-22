from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_text_emtpy_basket()
        self.should_not_have_product_in_basket()

    def should_be_text_emtpy_basket(self):
        basket_empty = self.get_text(*BasketPageLocators.BASKET_EMPTY)
        #print(basket_empty)
        assert basket_empty == 'Your basket is empty. Continue shopping', \
       "Empty basket message is not presented, but should be"

    def should_not_have_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PROCEED_BUTTON), \
       "Product in basket is presented, but should not be"
