import pytest
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def example_correct_user():
    return {'name': 'Юлия', 'login': 'yuliya_dershevich323333@yandex.ru', 'password': 'qwerty'}

@pytest.fixture
def example_new_user():
    return {'name': 'Юлия', 'login': 'yuliya_dershevich'+str(random.randint(10000, 99999))+'@yandex.ru', 'password': 'qwerty'}

@pytest.fixture
def example_not_correct_user():
    return {'name': '', 'login': 'yuliya_dershevich33@yandex.ru', 'password': 'qwert'}

@pytest.fixture(scope='function')
def driver():
    options = Options()
    options.add_argument('--window-size=1366,768')
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
    driver.get("https://stellarburgers.nomoreparties.site")
    yield driver
    driver.quit()