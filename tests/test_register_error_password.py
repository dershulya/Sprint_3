# Регистрация с ошибкой для некорректного пароля.

from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
import time

#открыть главную страницу
def test_register_error_password(driver, example_new_user, example_not_correct_user):
    # нажать кнопку Войти в аккаунт
    driver.find_element(*TestLocators.BUTTON_SIGN_IN).click()
    WebDriverWait(driver, 3)
    #нажать кнопку Зарегистрироваться
    driver.find_element(*TestLocators.BUTTON_REGISTRATION_ON_SIGN_IN).click()
    WebDriverWait(driver, 3)
    name_for_registration = example_new_user.get('name')
    mail_for_registration = example_new_user.get('login')
    password_for_registration = example_not_correct_user.get('password')
    #в поле Имя ввести "Юлия Дершевич"
    driver.find_element(*TestLocators.NAME_INPUT).send_keys(name_for_registration)
    #в поле Email ввести корректный адрес
    driver.find_element(*TestLocators.MAIL_INPUT).send_keys(mail_for_registration)
    #в поле Пароль ввести некорректный пароль из 5 символов "qwert"
    driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(password_for_registration)
    #нажать кнопку Зарегистрироваться
    driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
    time.sleep(2)
    # проверить наличие ошибки
    assert driver.find_element(*TestLocators.ERROR_PASSWORD).text == 'Некорректный пароль'

