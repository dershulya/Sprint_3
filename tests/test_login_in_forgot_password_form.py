# вход через кнопку в форме восстановления пароля

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

#открыть главную страницу
def test_login_button_sign_in(driver, example_correct_user):
    # нажать кнопку Войти в аккаунт
    driver.find_element(*TestLocators.BUTTON_SIGN_IN).click()
    WebDriverWait(driver, 3)
    # нажать кнопку Восстановить пароль
    driver.find_element(*TestLocators.BUTTON_RESTORE_PASSWORD).click()
    WebDriverWait(driver, 3)
    # нажать кнопку Войти
    driver.find_element(*TestLocators.BUTTON_LOGIN_ON_RESTORE_PASSWORD).click()
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
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(TestLocators.BUTTON_CHECKOUT))
    assert driver.find_element(*TestLocators.BUTTON_CHECKOUT).text == 'Оформить заказ'

