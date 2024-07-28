from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep


def test_different_langs_and_button_cart_exist(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    # Запускаем браузер
    browser.get(link)
    # Добавляем для наглядности sleep, чтобы проверяющий убедился в отображении название кнопки
    # добавления в корзину на нужном языке
    sleep(3)
    # если по данному css-селектору не будет найден элемент, то не будем выдавать ошибку,
    # а будем выдавать отсутствие кнопки на странице
    try:
        button = browser.find_element(By.CSS_SELECTOR, 'button.btn-add-to-basket')
        assert button.is_displayed(), "Button isn't displayed"
    except NoSuchElementException:
        # Для корректного отбражения кавычек и апострофа пришлось разбить на несколько строк
        assert False, "Button " + '"Add to cart"' + " isn't exist"


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()