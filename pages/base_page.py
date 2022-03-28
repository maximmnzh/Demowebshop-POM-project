import math

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from .locators import AccountLocators
from .locators import HeadersLocators


class BasePage(object):

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*HeadersLocators.LOGIN_LINK)
        link.click()

    def go_to_account_page(self):
        link = self.browser.find_element(*HeadersLocators.ACCOUNT_BUTTON)
        link.click()

    def go_to_change_pwd_page(self):
        link = self.browser.find_element(*AccountLocators.CHANGE_PASS_LINK)
        link.click()

    def log_out(self):
        link = self.browser.find_element(*HeadersLocators.LOG_OUT_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*HeadersLocators.LOG_OUT_LINK), (
            "Login link is not presented")
