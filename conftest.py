from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import pytest


@pytest.fixture(scope='function')
def browser(request):
    # забираем значение параметра language из команды запуска PyTest
    lang = request.config.getoption('language')
    # Добавляем запуск вебдрайвера с экспериментальной функцией переключения языка от Selenium
    chrome_options = Options()
    chrome_options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    # Собственные параметры запуска на локальной машине
    chrome_driver_path = "/usr/local/bin/chromedriver"
    chrome_options.binary_location = "/Applications/Google Chrome 114.app/Contents/MacOS/Google Chrome"
    service = Service(chrome_driver_path)
    print('Запускаем браузер')
    # Для запуска теста с локальной машины
    browser = webdriver.Chrome(service=service, options=chrome_options)
    # browser = webdriver.Chrome()
    yield browser
    print('\nЗакрываем браузер')
    # Закрываем браузер после окончания тестов
    browser.quit()

def pytest_addoption(parser):
    # добавляем парсер для получения параметров запуска команды bash
    parser.addoption('--language', action='store', help='Choose language', default='en')
