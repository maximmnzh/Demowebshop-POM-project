import pytest
from pages.locators import LinksLocators
from pages.login_page import LoginPage

email = 'test111222@test111222.com'
password = 'test111'


@pytest.mark.smoke
def test_should_be_email_field(browser):  # Проверка есть ли поле емаил
    page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
    page.open()
    page.should_be_email_field()


def test_should_be_password_field(browser):  # Проверка есть ли поле пароля
    page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
    page.open()
    page.should_be_password_field()


def test_should_be_login_button(browser):  # Проверка есть ли кнопка логина
    page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
    page.open()
    page.should_be_login_button()


def test_login(browser):  # Проверка логина
    page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
    page.open()
    page.login(email, password)
    page.should_be_login_result_page()


def test_should_be_login_result_page(browser):  # Проверка успешного логина
    page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
    page.open()
    page.should_be_login_result_page()
