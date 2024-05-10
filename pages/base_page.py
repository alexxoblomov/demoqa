import allure
from selenium.common import NoSuchElementException


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.browser.implicitly_wait(10)
        self.url = url

    def open(self):
        with allure.step("Открываем страницу"):
            self.browser.get(self.url)

    def is_element_present(self, how, what):
        with allure.step("Проверяем существование элемента"):
            try:
                self.browser.find_element(how, what)
            except NoSuchElementException:
                return False
            return True
