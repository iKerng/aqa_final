import pytest
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
from time import sleep


promo_link = ''
link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
# link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_link}'
link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

@pytest.mark.promo
def test_check_promotion(browser, link=link):
    product_page = ProductPage(browser, link)
    product_page.open()
    assert product_page.check_promotion(promo_name='newYear'), 'Открылась страница. Промо-акция отсуствует'


@pytest.mark.promo
def test_promotion_product_button_add_to_cart_exist(browser, link=link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_exist_button_cart()


@pytest.mark.params
@pytest.mark.parametrize(
    'promo_link',
    [pytest.param('bugged_link', marks=pytest.mark.xfail) if i == 7 else i for i in range(0, 10)]
)
def test_guest_can_add_product_to_basket(browser, promo_link, link=link):
    link = link + str(promo_link)
    product_link = (link.split('/'))[-2]
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.press_add_to_cart()
    product_page.solve_quiz_and_get_code()
    # product_page.go_to_cart()
    # sleep(10)
    product_page.should_be_added_to_cart(product_link)


@pytest.mark.this
def test_guest_can_add_product_to_basket_my(browser, link=link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.press_add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.go_to_cart()
    product_page.should_be_added_to_cart_my()

@pytest.mark.promo
def test_check_cost_of_cart_with_cost_of_product_added_to_cart(browser, link=link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.press_add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_matched_cost_cart_with_cost_book()


@pytest.mark.promo
def test_check_name_of_product_added_cart(browser, link=link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.press_add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_match_name_of_product_added_cart()


@pytest.mark.lang
def test_button_cart_exist(browser, link=link):
    product_page = ProductPage(browser, link)
    product_page.open()
    sleep(5)
    product_page.should_be_exist_button_cart()

@pytest.mark.waits
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link=link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.press_add_to_cart()
    product_page.should_not_get_succes_message()


@pytest.mark.waits
def test_guest_cant_see_success_message(browser, link=link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_get_succes_message()

@pytest.mark.waits
def test_message_disappeared_after_adding_product_to_basket(browser, link=link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.press_add_to_cart()
    product_page.should_not_is_not_element_present()