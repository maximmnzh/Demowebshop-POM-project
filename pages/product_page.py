from pages.locators import ItemsPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):
    def should_be_adding_button(self):
        assert self.is_element_present(*ItemsPageLocators.ADD_TO_CART_BUTTON), 'Adding to cart button not presented'

    def should_be_correct_books_link(self):
        expected_url = 'http://demowebshop.tricentis.com/books'
        actual_url = self.browser.current_url
        assert expected_url == actual_url, 'The link to all books is incorrect'

    def should_be_correct_item_link(self):
        expected_url = 'http://demowebshop.tricentis.com/health'
        actual_url = self.browser.current_url
        assert expected_url == actual_url, 'The link to the product is incorrect'

    def should_be_success_adding_massage(self):
        assert self.is_element_present(*ItemsPageLocators.SUCCESS_ADDING_MASSAGE), 'The addition of the product did not happen'

    def press_button_add_to_cart(self):
        self.browser.find_element(*ItemsPageLocators.ADD_TO_CART_BUTTON).click()
