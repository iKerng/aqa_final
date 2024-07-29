from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common import NoSuchElementException


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.browser.current_url.find('login') != -1, "Открытая страница не является страницей авторизации/регистрации"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        try:
            form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
            assert form.is_displayed(), "Форма логина отсутствует"
        except(NoSuchElementException):
            assert False, "NoSuchElementException: Форма логина отсутствует"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        try:
            form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
            assert form.is_displayed(), "Форма регистрации отсутствует"
        except(NoSuchElementException):
            assert False, "NoSuchElementException: Форма регистрации отсутствует"