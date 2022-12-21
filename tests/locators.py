from selenium.webdriver.common.by import By

class TestLocators:
    # поле ввода Имени при регистрации
    NAME_INPUT = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'
    # поле ввода Email при регистрации
    MAIL_INPUT = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[2]/div/div/input'
    # поле ввода Email при авторизации
    MAIL_LOGIN = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[1]/div/div/input'
    # поле ввода Пароля при регистрации
    PASSWORD_INPUT = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/div/input'
    # поле ввода Пароля при авторизации
    PASSWORD_LOGIN = By.XPATH, '// *[ @ id = "root"] / div / main / div / form / fieldset[2] / div / div / input'
    # кнопка "Зарегистрироваться" на странице регистрации
    BUTTON_REGISTRATION = By.XPATH, '//*[@id="root"]/div/main/div/form/button'
    # ошибка "Некорректный пароль"
    ERROR_PASSWORD = By.XPATH, '//*[@id="root"]/div/main/div/form/fieldset[3]/div/p'
    # кнопка "Войти" на странице авторизации
    BUTTON_LOGIN = By.XPATH, '//*[@id="root"]/div/main/div/form/button'
    # кнопка "Войти" в аккаунт на главной
    BUTTON_SIGN_IN = By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button'
    # кнопка "Зарегистрироваться" на странице авторизации
    BUTTON_REGISTRATION_ON_SIGN_IN = By.XPATH, '//*[@id="root"]/div/main/div/div/p[1]/a'
    # кнопка "Войти" на странице регистрации
    BUTTON_LOGIN_ON_REGISTRATION = By.XPATH, '//*[@id="root"]/div/main/div/div/p/a'
    # кнопка "Оформить заказ"
    BUTTON_CHECKOUT = By.XPATH, '//*[@id="root"]/div/main/section[2]/div/button'
    # кнопка "Личный кабинет"
    BUTTON_PRIVATE_OFFICE = By.XPATH, '//*[@id="root"]/div/header/nav/a/p'
    # кнопка "Восстановить пароль" на странице авторизации
    BUTTON_RESTORE_PASSWORD = By.XPATH, '//*[@id="root"]/div/main/div/div/p[2]/a '
    # кнопка "Войти" на странице восстановления пароля
    BUTTON_LOGIN_ON_RESTORE_PASSWORD = By.XPATH, '//*[@id="root"]/div/main/div/div/p/a '
    # кнопка "Конструктор" на странице личного кабинета
    BUTTON_CONSTRUCTOR = By.XPATH, '//*[@id="root"]/div/header/nav/ul/li[1]/a/p'
    # логотип "Stellar Burgers" на странице личного кабинета
    BUTTON_LOGO = By.XPATH, '//*[@id="root"]/div/header/nav/div'
    # кнопка "Выйти" на странице личного кабинета
    BUTTON_LOGOUT = By.XPATH, '//*[@id="root"]/div/main/div/nav/ul/li[3]/button'
    # кнопка "Булки" на странице Конструктор
    BUTTON_LOAF = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[1]'
    # кнопка "Соусы" на странице Конструктор
    BUTTON_SAUCE = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[2]'
    # кнопка "Начинки" на странице Конструктор
    BUTTON_FILLING = By.XPATH, '//*[@id="root"]/div/main/section[1]/div[1]/div[3]'