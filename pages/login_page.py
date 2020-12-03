from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Current page is not a login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self):
        registration_email = str(time.time()) + "@fakemail.org"
        registration_password = str(time.time())
        registration_email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(registration_email)
        registration_password1_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1).send_keys(registration_password)
        registration_password2_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2).send_keys(registration_password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()