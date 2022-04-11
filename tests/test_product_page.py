import time

import pytest

from pages.dataset import TestDatasets, register_dataset
from pages.locators import LinksLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.register_page import RegisterPage


@pytest.mark.fields
class TestProductPageFields:
    def test_should_be_correct_books_link(self, browser):  # Проверка корректной ссылки на все товары
        page = ProductPage(browser, LinksLocators.BOOKS_LINK)
        page.open()
        page.should_be_correct_books_link()

    def test_should_be_correct_item_link(self, browser):  # Проверка корректной ссылки на health book
        page = ProductPage(browser, LinksLocators.BOOKS_HEALTH_ITEM_LINK)
        page.open()
        page.should_be_correct_item_link()

    def test_should_be_adding_button(self, browser):  # Проверка, есть ли кнопка добавления товара
        page = ProductPage(browser, LinksLocators.BOOKS_HEALTH_ITEM_LINK)
        page.open()
        page.should_be_adding_button()


@pytest.mark.smoke
class TestAddingItemToCart:
    def test_adding_item_to_cart(self, browser):  # Добавление товара со страницы деталей товара
        page = ProductPage(browser, LinksLocators.BOOKS_HEALTH_ITEM_LINK)
        page.open()
        page.press_button_add_to_cart()
        page.should_be_success_adding_massage()

    def test_adding_item_from_all_product(self, browser):  # Добавление товара со страницы списка товаров
        page = ProductPage(browser, LinksLocators.BOOKS_LINK)
        page.open()
        page.press_button_add_from_all_books()
        page.should_be_success_adding_massage()

    def test_change_quantity_item(self, browser):  # Изменение количества товара в корзине и перерасчет корзины
        page = ProductPage(browser, LinksLocators.BOOKS_LINK)
        page.open()
        page.press_button_add_from_all_books()
        page.should_be_success_adding_massage()
        page.press_go_to_cart_button()
        page.change_quantity_of_item()
        page.press_update_cart_button()


@pytest.mark.smoke1
class TestCheckoutOrder:
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        page = RegisterPage(browser, LinksLocators.REGISTER_PAGE_LINK)
        page.open()
        first_name, last_name, email, password = register_dataset()
        page.register_new_user(first_name, last_name, email, password)
        page.should_be_register_result_page()
        page.log_out()
        return email, password

    def test_checkout_order_with_login(self, browser, setup):  # Проверка оформления заказа и логина на готовых данных
        page = LoginPage(browser, LinksLocators.LOGIN_PAGE_LINK)
        page.open()
        page.login(email=setup[0], password=setup[1])
        page.should_be_login_result_page()
        page = ProductPage(browser, LinksLocators.BOOKS_HEALTH_ITEM_LINK)
        page.open()
        page.press_button_add_to_cart()
        page.should_be_success_adding_massage()
        page.press_go_to_cart_button()
        page.change_quantity_of_item()
        page.press_update_cart_button()
        page.press_to_agree_checkbox()
        page.press_to_checkout_button()
        time.sleep(2)
        page.making_order()
        page.should_be_confirm_order_result_page()



