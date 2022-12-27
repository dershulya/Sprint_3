# выход по кнопке «Выйти» в личном кабинете

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TestLocators

#открыть главную страницу
def test_logout_in_private_office(driver, example_correct_user):
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
    WebDriverWait(driver, 3)
    # нажать кнопку Личный кабинет
    driver.find_element(*TestLocators.BUTTON_PRIVATE_OFFICE).click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located(TestLocators.BUTTON_LOGOUT))
    # нажать кнопку Выход
    driver.find_element(*TestLocators.BUTTON_LOGOUT).click()
    #проверить url страницы
    WebDriverWait(driver, 5).until_not(EC.url_to_be('https://stellarburgers.nomoreparties.site/account/profile'))
    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

