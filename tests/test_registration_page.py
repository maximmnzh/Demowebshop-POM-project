import pytest
from pages.locators import LinksLocators
from pages.register_page import RegisterPage
from pages.dataset import register_dataset


@pytest.mark.fields
class TestRegistrationPageFields:
    def test_should_be_gender_radiobuttons(self, browser):  # Проверка есть ли чекбоксы
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        page.should_be_gender_radiobuttons()

    def test_should_be_firstname_field(self, browser):  # Проверка есть ли поле имени
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        page.should_be_firstname_field()

    def test_should_be_lastname_field(self, browser):  # Проверка есть ли поле фамилии
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        page.should_be_lastname_field()

    def test_should_be_email_field(self, browser):  # Проверка есть ли поле емаил
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        page.should_be_email_field()

    def test_should_be_password_field(self, browser):  # Проверка есть ли поле пароля
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        page.should_be_password_field()

    def test_should_be_confirm_password_field(self, browser):  # Проверка есть ли поле пароля
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        page.should_be_confirm_password_field()

    def test_should_see_register_button(self, browser):  # Проверка есть ли кнопка регистрации
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        page.should_be_register_button()


@pytest.mark.smoke
class TestRegistrationNewUser:
    def test_registration_new_user(self, browser):  # Проверка регистрации и подтверждения регистрации
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        first_name, last_name, email, password = register_dataset()
        page.register_new_user(first_name, last_name, email, password)
        page.should_be_register_result_page()
