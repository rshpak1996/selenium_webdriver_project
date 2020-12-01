from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
        def should_be_login_url(self):
        # реалізуйте перевірку на корректну адресу
        assert "login" in self.browsere.current_url, "Current page is not a login page"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()