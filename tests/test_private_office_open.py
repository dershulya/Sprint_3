# переход по клику на «Личный кабинет»

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

#открыть главную страницу
def test_private_office_open(driver, example_correct_user):
    # нажать кнопку Войти в аккаунт
    driver.find_element(*TestLocators.BUTTON_SIGN_IN).click()
    WebDriverWait(driver, 3)
    mail_for_login = example_correct_user.get('login')
    password_for_login = example_correct_user.get('password')
    #в поле Email ввести корректный адрес
    driver.find_element(*TestLocators.MAIL_LOGIN).clear()
    driver.find_element(*TestLocators.MAIL_LOGIN).send_keys(mail_for_login)
    #в поле Пароль ввести корректный пароль из 6 символов "qwerty"
    driver.find_element(*TestLocators.PASSWORD_LOGIN).clear()
    driver.find_element(*TestLocators.PASSWORD_LOGIN).send_keys(password_for_login)
    #нажать кнопку Войти
    driver.find_element(*TestLocators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(EC.url_to_be('https://stellarburgers.nomoreparties.site/'))
    # нажать кнопку Личный кабинет
    driver.find_element(*TestLocators.BUTTON_PRIVATE_OFFICE).click()
    #проверить url страницы
    WebDriverWait(driver, 10).until_not(EC.url_to_be('https://stellarburgers.nomoreparties.site'))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account"

