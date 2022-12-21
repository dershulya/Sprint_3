# вход через кнопку в форме регистрации

from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
import time

#открыть главную страницу
def test_login_in_register_form(driver, example_correct_user):
    # нажать кнопку Войти в аккаунт
    driver.find_element(*TestLocators.BUTTON_SIGN_IN).click()
    WebDriverWait(driver, 3)
    #нажать кнопку Зарегистрироваться
    driver.find_element(*TestLocators.BUTTON_REGISTRATION_ON_SIGN_IN).click()
    WebDriverWait(driver, 3)
    # нажать кнопку Войти
    driver.find_element(*TestLocators.BUTTON_LOGIN_ON_REGISTRATION).click()
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
    #проверить, что появилась кнопка Оформить заказ
    time.sleep(2)
    assert driver.find_element(*TestLocators.BUTTON_CHECKOUT).text == 'Оформить заказ'

