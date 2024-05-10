import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    print("\nstart chrome browser for test...")
    yield browser
    print("\nquit browser...")
    browser.quit()

