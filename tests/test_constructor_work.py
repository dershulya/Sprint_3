# Проверка, что работают переходы к разделам: «Булки», «Соусы», «Начинки».

from locators import TestLocators

#открыть главную страницу
def test_constructor_work_click_loaf(driver):
    #получаем атрибуты ненажатых кнопок "Соусы" и "Начинки"
    sause_off = driver.find_element(*TestLocators.BUTTON_SAUCE).get_attribute('class')
    filling_off = driver.find_element(*TestLocators.BUTTON_FILLING).get_attribute('class')
    #нажать кнопку Соусы
    driver.find_element(*TestLocators.BUTTON_SAUCE).click()
    # получаем атрибут нажатой кнопки "Соусы"
    sause_on = driver.find_element(*TestLocators.BUTTON_SAUCE).get_attribute('class')
    # нажать кнопку Начинки
    driver.find_element(*TestLocators.BUTTON_FILLING).click()
    # получаем атрибут нажатой кнопки "Начинки"
    filling_on = driver.find_element(*TestLocators.BUTTON_FILLING).get_attribute('class')
    # получаем атрибут ненажатой кнопки "Булки"
    loaf_off = driver.find_element(*TestLocators.BUTTON_LOAF).get_attribute('class')
    # нажать кнопку Булки
    driver.find_element(*TestLocators.BUTTON_LOAF).click()
    # получаем атрибут нажатой кнопки "Булки"
    loaf_on = driver.find_element(*TestLocators.BUTTON_LOAF).get_attribute('class')

    #проверить, что атрибут class не совпадает у нажатых и ненажатых кнопок
    assert sause_off != sause_on
    assert filling_off != filling_on
    assert loaf_off != loaf_on

