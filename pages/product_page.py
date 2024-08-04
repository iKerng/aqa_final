from .base_page import BasePage
from .locators import ProductPageLocators
from math import log, sin
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
from re import sub

class ProductPage(BasePage):
    def should_be_exist_button_cart(self):
        # если по данному css-селектору не будет найден элемент, то не будем выдавать ошибку,
        # а будем выдавать отсутствие кнопки на странице
        res = self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CART)
        assert res[0], res[1] + "Button add to cart is not present."


    def press_add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART).click()


    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        arr_alert_text = alert_text.split('\n')
        x = int((arr_alert_text[0].split(' '))[-2])
        res = str(eval((arr_alert_text[1].replace('?', '').replace('log10', 'log').split(' '))[-1]))
        alert.send_keys(res)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")


    def go_to_cart(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_GO_TO_CART).click()


    def should_be_added_to_cart_my(self):
        try:
            self.browser.find_element(*ProductPageLocators.CART_IS_NOT_EMPTY)
            assert True
        except NoSuchElementException:
            assert False, 'Корзина пуста'


    def should_be_added_to_cart(self, product_link):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_alert = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ALERT).text
        assert product_name == product_name_in_alert, f'Название книги, в алерте отличается: <{product_name_in_alert}>'


    def should_be_match_name_of_product_added_cart(self, product_link):
        name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        self.go_to_cart()
        name_in_cart = (self.browser.
                        find_element(*ProductPageLocators.PRODUCT_NAME_IN_CART(href_product=product_link)).text)
        assert name_product == name_in_cart, 'Наименование товара в корзине отличается от наименования добавляемого товара'


    def should_be_matched_cost_cart_with_cost_book(self):
        cost_product = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text.replace(',', '.')
        cost_product = float(sub(r'[^0-9.,]', '', cost_product))
        self.go_to_cart()
        cost_in_cart = self.browser.find_element(*ProductPageLocators.CART_PRODUCT_COST).text.replace(',', '.')
        cost_in_cart = float(sub(r'[^0-9.,]', '', cost_in_cart))
        assert cost_product == cost_in_cart, 'Цена товара в корзине отличается от цены добавляемого товара'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"


    def should_not_get_succes_message(self):
        assert self.is_not_element_present(loc=ProductPageLocators.PRODUCT_NAME_IN_ALERT)\
            , 'Сообщение об успехе присутствует'


    def should_not_is_not_element_present(self):
        assert self.is_disappeared(loc=ProductPageLocators.PRODUCT_NAME_IN_ALERT)\
            , 'Сообщение об успехе присутствует'