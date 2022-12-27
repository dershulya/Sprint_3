from selenium.webdriver.common.by import By

class TestLocators:
    # поле ввода Имени при регистрации
    NAME_INPUT = By.XPATH, '//label[.="Имя"]/parent::*/input'
    # поле ввода Email при регистрации
    MAIL_INPUT = By.XPATH, '//label[.="Email"]/parent::*/input'
    # поле ввода Email при авторизации
    MAIL_LOGIN = By.XPATH, '//label[.="Email"]/parent::*/input'
    # поле ввода Пароля при регистрации
    PASSWORD_INPUT = By.XPATH, '//label[.="Пароль"]/parent::*/input'
    # поле ввода Пароля при авторизации
    PASSWORD_LOGIN = By.XPATH, '//label[.="Пароль"]/parent::*/input'
    # кнопка "Зарегистрироваться" на странице регистрации
    BUTTON_REGISTRATION = By.XPATH, '//*[@id="root"]/div/main/div/form/button'
    # ошибка "Некорректный пароль"
    ERROR_PASSWORD = By.CSS_SELECTOR, ".input__error"
    # кнопка "Войти" на странице авторизации
    BUTTON_LOGIN = By.XPATH, '//*[@id="root"]/div/main/div/form/button'
    # кнопка "Войти" в аккаунт на главной
    BUTTON_SIGN_IN = By.XPATH, '//button[.="Войти в аккаунт"]'
    # кнопка "Зарегистрироваться" на странице авторизации
    BUTTON_REGISTRATION_ON_SIGN_IN = By.XPATH, '//a[.="Зарегистрироваться"]'
    # кнопка "Войти" на странице регистрации
    BUTTON_LOGIN_ON_REGISTRATION = By.XPATH, '//a[.="Войти"]'
    # кнопка "Оформить заказ"
    BUTTON_CHECKOUT = By.XPATH, '//button[.="Оформить заказ"]'
    # кнопка "Личный кабинет"
    BUTTON_PRIVATE_OFFICE = By.XPATH, '//*[@id="root"]/div/header/nav/a/p'
    # кнопка "Восстановить пароль" на странице авторизации
    BUTTON_RESTORE_PASSWORD = By.XPATH, './/a[.="Восстановить пароль"]'
    # кнопка "Войти" на странице восстановления пароля
    BUTTON_LOGIN_ON_RESTORE_PASSWORD = By.XPATH, '//a[.="Войти"]'
    # кнопка "Конструктор" на странице личного кабинета
    BUTTON_CONSTRUCTOR = By.XPATH, './/p[.="Конструктор"]'
    # логотип "Stellar Burgers" на странице личного кабинета
    BUTTON_LOGO = By.XPATH, '//*[@id="root"]/div/header/nav/div'
    # кнопка "Выйти" на странице личного кабинета
    BUTTON_LOGOUT = By.XPATH, './/button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]'
    # кнопка "Булки" на странице Конструктор
    BUTTON_LOAF =  By.XPATH, '//div[.="Булки"]'
    # кнопка "Соусы" на странице Конструктор
    BUTTON_SAUCE = By.XPATH, '//div[.="Соусы"]'
    # кнопка "Начинки" на странице Конструктор
    BUTTON_FILLING = By.XPATH, '//div[.="Начинки"]'