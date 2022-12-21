# Успешная регистрация.
# Поле «Имя» должно быть не пустым; в поле Email введён email в формате логин@домен:
# Минимальный пароль — шесть символов.

from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
import time

#открыть главную страницу
def test_register_successful(driver, example_new_user):
    # нажать кнопку Войти в аккаунт
    driver.find_element(*TestLocators.BUTTON_SIGN_IN).click()
    WebDriverWait(driver, 3)
    #нажать кнопку Зарегистрироваться
    driver.find_element(*TestLocators.BUTTON_REGISTRATION_ON_SIGN_IN).click()
    WebDriverWait(driver, 3)
    name_for_registration = example_new_user.get('name')
    mail_for_registration = example_new_user.get('login')
    password_for_registration = example_new_user.get('password')
    #в поле Имя ввести "Юлия Дершевич"
    driver.find_element(*TestLocators.NAME_INPUT).send_keys(name_for_registration)
    #в поле Email ввести корректный адрес
    driver.find_element(*TestLocators.MAIL_INPUT).send_keys(mail_for_registration)
    #в поле Пароль ввести корректный пароль из 6 символов "qwerty"
    driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(password_for_registration)
    #нажать кнопку Зарегистрироваться
    driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
    #проверить url страницы
    time.sleep(2)
    assert driver.current_url== "https://stellarburgers.nomoreparties.site/login"

