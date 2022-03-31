import pytest
from pages.locators import LinksLocators
from pages.main_page import MainPage


@pytest.mark.smoke
@pytest.mark.fields
class TestMainPageLinks:
    def test_should_be_basic_links(self, browser):
        page = MainPage(browser, LinksLocators.MAIN_PAGE_LINK)
        page.open()
        page.should_be_register_button()
        page.should_be_login_button()
        page.should_be_cart_button()
        page.should_be_wishlist_button()
