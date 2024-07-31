from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    BUTTON_GO_TO_CART = (By.CSS_SELECTOR, 'div.container-fluid.page div.alert-info a[href*="basket"]')
    CART_IS_NOT_EMPTY = (By.CSS_SELECTOR, '#content_inner div.row')
    # todo переделать селектор, так как он зависит от линка, то есть убрать хардкод
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main>h1')
    CART_PRODUCT_COST = (By.CSS_SELECTOR, 'div.basket-items div.col-sm-1 > p.price_color')
    PRODUCT_COST = (By.CSS_SELECTOR, 'div.product_main p.price_color')


    def PRODUCT_NAME_IN_CART(self, href_product):
        return (By.CSS_SELECTOR, f'div.col-sm-4 a[href*="{href_product}"]')
