from pages.locators import LoginLocators
from pages.locators import HeadersLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def should_be_email_field(self):
        assert self.is_element_present(*LoginLocators.EMAIL_FIELD), "Email field not presented"

    def should_be_password_field(self):
        assert self.is_element_present(*LoginLocators.PASSWORD_FIELD), "Password field not presented"

    def should_be_login_button(self):
        assert self.is_element_present(*LoginLocators.LOGIN_BUTTON), 'Login button not presented'

    def login(self, email, password):
        self.browser.find_element(*LoginLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginLocators.LOGIN_BUTTON).click()

    def should_be_login_result_page(self):
        assert self.browser.find_element(*HeadersLocators.ACCOUNT_BUTTON), 'Not logged in'





















('\n'
 'def test_login_existing_user(browser):\n'
 '    page = RegisterPage(browser, LinksLocators.MAIN_PAGE_LINK)\n'
 '    page.open()\n'
 '    page.go_to_login_page()\n'
 '    page.log_in(email, pwd)\n'
 '\n'
 '\n'
 'def test_user_can_change_pass(browser):\n'
 '    page = RegisterPage(browser, LinksLocators.MAIN_PAGE_LINK)\n'
 '    page.open()\n'
 '    page.go_to_login_page()\n'
 '    page.log_in(email, pwd)\n'
 '    page.go_to_account_page()\n'
 '    page.go_to_change_pass_page()\n'
 '    page.change_pass(pwd, pwd)\n'
 '    page.should_be_success_pass_change()\n'
 '\n'
 '\n'
 'def log_in(self, email, password):\n'
 '    self.browser.find_element(*RegisterLocators.EMAIL_FIELD).send_keys(email)\n'
 '    self.browser.find_element(*RegisterLocators.PASSWORD_FIELD).send_keys(password)\n'
 '    self.browser.find_element(*RegisterLocators.LOG_IN_BUTTON).click()\n'
 '\n'
 '\n'
 'def change_pass(self, old_pass, new_pass):\n'
 '    self.browser.find_element(*AccountLocators.OLD_PASS_FIELD).send_keys(old_pass)\n'
 '    self.browser.find_element(*AccountLocators.NEW_PASS_FIELD).send_keys(new_pass)\n'
 '    self.browser.find_element(*AccountLocators.NEW_PASS_REPEAT_FIELD).send_keys(new_pass)\n'
 '    self.browser.find_element(*AccountLocators.CHANGE_PASS_BUTTON).click()\n'
 '\n'
 '\n'
 'def should_be_success_pass_change(self):\n'
 '    result_message = self.browser.find_element(*AccountLocators.CHANGE_PASS_RESULT).text\n'
 '    print(result_message)\n'
 '    assert result_message == "Password was changed", \'result message is not looking good\'\n')