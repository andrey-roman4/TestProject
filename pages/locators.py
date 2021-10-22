from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    LOGIN_LINK_NAME = 'login'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM =  (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.add-to-basket')
    PRODUCT_NAME_TITLE = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_NAME_ADDED_TO_BASKET = (By.CSS_SELECTOR, '#messages :first-child .alertinner strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRICE_PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, '.alert-info strong')
    SUCCES_MESSAGE = (By.CSS_SELECTOR, '#messages :first-child .alertinner')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_LINK = (By.PARTIAL_LINK_TEXT, 'basket')
    BASKET_EMPTY = (By.CSS_SELECTOR, 'div#content_inner p')
    BASKET_PROCEED_BUTTON = (By.CSS_SELECTOR, '.btn-block')
