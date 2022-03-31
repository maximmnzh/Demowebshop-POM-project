import pytest
from pages.locators import CustomerLocators, LinksLocators
from pages.changepassword_page import ChangepasswordPage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


class TestLoginAfterRegistration:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        first_name, last_name, email, password = page.register_dataset()
        page.register_new_user(first_name, last_name, email, password)
        page.should_be_register_result_page()
        return email, password

    def test_change_password(self, browser, setup):  # Проверка смены пароля
        page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
        page.open()
        page.login(email=setup[0], password=setup[1])
        page = ChangepasswordPage(browser, LinksLocators.CHANGE_PASS_LINK)
        page.open()
        page.change_password(password=setup[1], new_password='test1234')
        page.should_be_change_pass_result()

    def test_fields(self, browser, setup):  # Проверка полей
        page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
        page.open()
        page.login(email=setup[0], password=setup[1])
        page = ChangepasswordPage(browser, LinksLocators.CHANGE_PASS_LINK)
        page.open()
        page.should_be_old_password_field()
        page.should_be_new_password_field()
        page.should_be_confirm_password_field()
        page.should_be_change_password_button()

