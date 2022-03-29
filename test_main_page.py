import pytest
from .pages.locators import MAIN_PAGE_LINK
from .pages.main_page import MainPage


@pytest.mark.smoke
def test_should_be_basic_links(browser):
    page = MainPage(browser, MAIN_PAGE_LINK)
    page.open()
    page.should_be_register_button()
    page.should_be_login_button()
    page.should_be_cart_button()
    page.should_be_wishlist_button()
