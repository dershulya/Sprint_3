# переход по клику на «Конструктор» и на логотип Stellar Burgers

from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
import time

#открыть главную страницу
def test_constructor_open_tab_constructor(driver, example_correct_user):
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
    time.sleep(2)
    # нажать кнопку Личный кабинет
    driver.find_element(*TestLocators.BUTTON_PRIVATE_OFFICE).click()
    time.sleep(2)
    # нажать кнопку Конструктор
    driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
    #проверить url страницы
    time.sleep(2)
    assert driver.current_url== "https://stellarburgers.nomoreparties.site/"

def test_constructor_open_tab_logo(driver, example_correct_user):
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
    time.sleep(2)
    # нажать кнопку Личный кабинет
    driver.find_element(*TestLocators.BUTTON_PRIVATE_OFFICE).click()
    time.sleep(2)
    # нажать на логотип Stellar Burgers
    driver.find_element(*TestLocators.BUTTON_LOGO).click()
    #проверить url страницы
    time.sleep(2)
    assert driver.current_url== "https://stellarburgers.nomoreparties.site/"

