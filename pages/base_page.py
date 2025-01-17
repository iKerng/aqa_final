from conftest import browser
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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

    def is_not_element_present(self, loc, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(loc))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, loc, timeout=4):
        try:
            (WebDriverWait(self.browser, timeout, 1, TimeoutException)
             .until_not(EC.presence_of_element_located(loc)))
        except TimeoutException:
            return False
        return True
