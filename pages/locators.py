from selenium.webdriver.common.by import By


class LinksLocators(object):
    MAIN_PAGE_LINK = 'http://demowebshop.tricentis.com'
    REGISTER_PAGE_LINK = 'http://demowebshop.tricentis.com/register'
    LOGIN_PAGE_LINK = "http://demowebshop.tricentis.com/login"
    CHANGE_PASS_LINK = 'http://demowebshop.tricentis.com/customer/changepassword'
    BOOKS_HEALTH_ITEM_LINK = 'http://demowebshop.tricentis.com/health'
    BOOKS_LINK = 'http://demowebshop.tricentis.com/books'


class HeadersLocators(object):
    REGISTER_BUTTON = (By.CSS_SELECTOR, ".ico-register")
    LOGIN_LINK = (By.CSS_SELECTOR, ".ico-login")
    CART_LINK = (By.CSS_SELECTOR, ".ico-cart")
    WISHLIST_BUTTON = (By.CSS_SELECTOR, ".ico-wishlist")
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, '.account')
    LOG_OUT_LINK = (By.CSS_SELECTOR, '.ico-logout')


class RegisterLocators(object):
    MALE_RADIOBUTTON = (By.CSS_SELECTOR, '#gender-male')
    FEMALE_RADIOBUTTON = (By.CSS_SELECTOR, '#gender-female')
    FIRSTNAME_FIELD = (By.CSS_SELECTOR, '#FirstName')
    LASTNAME_FIELD = (By.CSS_SELECTOR, '#LastName')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#Email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#Password')
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, '#ConfirmPassword')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register-button')


class LoginLocators(object):
    EMAIL_FIELD = (By.CSS_SELECTOR, '#Email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#Password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.login-button')


class CustomerLocators(object):
    CHANGE_PASS_LINK = (By.CSS_SELECTOR, 'li:nth-child(7) .inactive')
    OLD_PASS_FIELD = (By.CSS_SELECTOR, '#OldPassword')
    NEW_PASS_FIELD = (By.CSS_SELECTOR, '#NewPassword')
    CONFIRM_PASS_FIELD = (By.CSS_SELECTOR, '#ConfirmNewPassword')
    CHANGE_PASS_BUTTON = (By.CSS_SELECTOR, '.change-password-button')
    CHANGE_PASS_RESULT = (By.CSS_SELECTOR, '.result')


class ItemsPageLocators(object):
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#add-to-cart-button-22')
    ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, '#add-to-wishlist-button-22')
    SUCCESS_ADDING_MASSAGE = (By.CSS_SELECTOR, '.success')
    ADD_TO_CART_FROM_ALL_PRODUCT = (By.CSS_SELECTOR, '.product-box-add-to-cart-button')
    QUANTITY_ITEMS_FIELD = (By.CSS_SELECTOR, '.qty-input')
    UPDATE_CART_BUTTON = (By.CSS_SELECTOR, '.update-cart-button')
    TOTAL_ORDER_PRICE_FIELD = (By.CSS_SELECTOR, '.order-total')
