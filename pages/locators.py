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
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main>h1')
    PRODUCT_NAME_IN_ALERT = (By.CSS_SELECTOR, 'div#messages > div.alert:nth-child(1) > .alertinner > strong')
    CART_PRODUCT_NAME = (By.CSS_SELECTOR, 'div#messages div.alert-success div.alertinner strong')
    CART_PRODUCT_COST = (By.CSS_SELECTOR, 'div.basket-items div.col-sm-1 > p.price_color')
    PRODUCT_COST = (By.CSS_SELECTOR, 'div.product_main p.price_color')


    def PRODUCT_NAME_IN_CART(href_product):
        print(f'href_product=<{href_product}>')
        print(f'div.col-sm-4 a[href*="{href_product}"]')
        return (By.CSS_SELECTOR, f'div.col-sm-4 a[href*="{href_product}"]')
