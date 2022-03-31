import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

