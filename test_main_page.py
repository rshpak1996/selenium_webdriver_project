from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest

# pytest -v --tb=line --language=en test_main_page.py

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)      # ініціалізуєм Page Object, передаєм в конструктор екземпляр драйвера і url адресу
        page.open()                         # відкриваєм сторінку
        page.should_be_login_link()         # перевіряємо наявнність посилання на сторінку логіна
        page.go_to_login_page()             # виконуєм метод сторінки - переходимо на сторінку логіна
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_not_be_items_in_basket()
        basket_page.should_be_empty_basket_text()
