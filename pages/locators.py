from selenium.webdriver.common.by import By

MAIN_PAGE_LINK = 'http://demowebshop.tricentis.com'
REGISTER_PAGE_LINK = 'http://demowebshop.tricentis.com/register'
CHANGE_PASS_LINK = 'http://demowebshop.tricentis.com/customer/changepassword'


class HeadersLocators(object):
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".ico-register")
    LOGIN_LINK = (By.CSS_SELECTOR, ".ico-login")
    CART_LINK = (By.CSS_SELECTOR, ".ico-cart")
    WISHLIST_BUTTON = (By.CSS_SELECTOR, ".ico-wishlist")
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, '.account')
    LOG_OUT_LINK = (By.CSS_SELECTOR, '.ico-logout')


class RegisterLocators(object):
    REGISTER_FIELD = (By.CSS_SELECTOR, '.center-2')
    MALE_RADIOBUTTON = (By.CSS_SELECTOR, '#gender-male')
    FEMALE_RADIOBUTTON = (By.CSS_SELECTOR, '#gender-female')
    FIRSTNAME_FIELD = (By.CSS_SELECTOR, '#FirstName')
    LASTNAME_FIELD = (By.CSS_SELECTOR, '#LastName')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#Email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#Password')
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, '#ConfirmPassword')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register-button')
    LOG_IN_BUTTON = (By.CSS_SELECTOR, '.login-button')


class AccountLocators(object):
    CHANGE_PASS_LINK = (By.CSS_SELECTOR, 'li:nth-child(7) .inactive')
    OLD_PASS_FIELD = (By.CSS_SELECTOR, '#OldPassword')
    NEW_PASS_FIELD = (By.CSS_SELECTOR, '#NewPassword')
    NEW_PASS_REPEAT_FIELD = (By.CSS_SELECTOR, '#ConfirmNewPassword')
    CHANGE_PASS_BUTTON = (By.CSS_SELECTOR, '.change-password-button')
    CHANGE_PASS_RESULT = (By.CSS_SELECTOR, '.result')