import pytest
from pages.locators import LinksLocators, ItemsPageLocators
from pages.product_page import ProductPage


@pytest.mark.fields
class TestProductPageFields:
    def test_should_be_correct_books_link(self, browser):
        page = ProductPage(browser, LinksLocators.BOOKS_LINK)
        page.open()
        page.should_be_correct_books_link()

    def test_should_be_correct_item_link(self, browser):
        page = ProductPage(browser, LinksLocators.BOOKS_HEALTH_ITEM_LINK)
        page.open()
        page.should_be_correct_item_link()

    def test_should_be_adding_button(self, browser):
        page = ProductPage(browser, LinksLocators.BOOKS_HEALTH_ITEM_LINK)
        page.open()
        page.should_be_adding_button()


@pytest.mark.smoke
class TestAddingItemToCart:
    def test_adding_item_to_cart(self, browser):
        page = ProductPage(browser, LinksLocators.BOOKS_HEALTH_ITEM_LINK)
        page.open()
        page.press_button_add_to_cart()
        page.should_be_success_adding_massage()
