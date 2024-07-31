from conftest import browser
from selenium.common.exceptions import NoSuchElementException


class BasePage():
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
            return [False, 'NoSuchElementException: ']
        return [True]


    def check_promotion(self, promo_name):
        return self.browser.current_url.find('promo=' + promo_name) != -1