import pytest
from pages.locators import LinksLocators
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


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
    def test_login(self, browser):  # Проверка логина на готовых данных
        page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
        page.open()
        page.login(email="test111222@test111222.com", password="test123")
        page.should_be_login_result_page()


@pytest.mark.smoke
class TestLoginAfterRegistration:  # Проверка логина на новых, рандомных данных
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        first_name, last_name, email, password = page.register_dataset()
        page.register_new_user(first_name, last_name, email, password)
        page.should_be_register_result_page()
        page.log_out()
        return email, password

    def test_login(self, browser, setup):
        page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
        page.open()
        page.login(email=setup[0], password=setup[1])
        page.should_be_login_result_page()
