from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_add_to_basket_success_text(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_success_text = self.browser.find_element(*ProductPageLocators.PRODUCT_SUCCESS_TEXT).text
        assert product_name == product_success_text, "Success text are not the same with product name"

    def should_be_equal_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_total_price = self.browser.find_element(*ProductPageLocators.PRODUCT_TOTAL_PRICE).text
        assert product_price == product_total_price, "Prices doesn't equal"