from selenium.webdriver.common.by import By

class AccountPageLocators:
    PROFILE_BUTTON = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(),'Выход')]")
    LOGIN_BUTTON = (By.XPATH, '//button[contains(text(),"Войти")]')
    EMAIL_FIELD = (By.XPATH, "//input[@name='name']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")
    LOGIN_AFTER_LOGOUT = (By.XPATH, "//h2[contains(text(),'Вход')]")
