import pytest
from pages.locators import LinksLocators
from pages.login_page import LoginPage


@pytest.mark.fields
class TestLoginPageFields:
    def test_should_be_email_field(self, browser):  # Проверка есть ли поле емаил
        page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
        page.open()
        page.should_be_email_field()

    def test_should_be_password_field(self, browser):  # Проверка есть ли поле пароля
        page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
        page.open()
        page.should_be_password_field()

    def test_should_be_login_button(self, browser):  # Проверка есть ли кнопка логина
        page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
        page.open()
        page.should_be_login_button()


@pytest.mark.smoke
class TestLogin:
    def test_login(self, browser):  # Проверка логина
        page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
        page.open()
        page.login(email="test111222@test111222.com", password="test123")
        page.should_be_login_result_page()
