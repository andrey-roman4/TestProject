from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_current_link(LoginPageLocators.LOGIN_LINK_NAME), "Current page is not login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented" # реализуйте проверку, что есть форма логина

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented" # реализуйте проверку, что есть форма регистрации на странице
        
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INPUT)
        email_input.send_keys(email)
        password_input1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT1)
        password_input1.send_keys(password)
        password_input2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT2)
        password_input2.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()
