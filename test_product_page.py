import pytest
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
from time import sleep



@pytest.mark.promo
def test_check_promotion(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    product_page = ProductPage(browser, link)
    product_page.open()
    assert product_page.check_promotion(promo_name='newYear'), 'Открылась страница. Промо-акция отсуствует'


@pytest.mark.promo
def test_promotion_product_button_add_to_cart_exist(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_exist_button_cart()


@pytest.mark.promo
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.press_add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.go_to_cart()
    product_page.should_be_added_to_cart()


@pytest.mark.promo
def test_check_cost_of_cart_with_cost_of_product_added_to_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.press_add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_matched_cost_cart_with_cost_book()


@pytest.mark.promo
def test_check_name_of_product_added_cart(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    product_link = (link.split('/'))[-2]
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.press_add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_match_name_of_product_added_cart(product_link)


@pytest.mark.lang
def test_button_cart_exist(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(browser, link)
    product_page.open()
    sleep(5)
    product_page.should_be_exist_button_cart()