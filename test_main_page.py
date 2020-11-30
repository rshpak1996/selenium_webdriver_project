# pytest -v --tb=line --language=en test_main_page.py
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)      # ініціалізуєм Page Object, передаєм в конструктор екземпляр драйвера і url адресу
    page.open()                         # відкриваєм сторінку
    page.should_be_login_link()         # перевіряємо наявнність посилання на сторінку логіна
    # page.go_to_login_page()             # виконуєм метод сторінки - переходимо на сторінку логіна