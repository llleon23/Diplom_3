import allure
from .base_page import BasePage
from locators.profile_locators import AccountPageLocators

class AccountPage(BasePage):
    @allure.step("Кликнуть на кнопку профиля")
    def click_profile_button(self):
        self.click_when_clickable(AccountPageLocators.PROFILE_BUTTON)

    @allure.step("Выполнить вход в систему")
    def login(self, email, password):
        self.add_text_to_element(AccountPageLocators.EMAIL_FIELD, email)
        self.add_text_to_element(AccountPageLocators.PASSWORD_FIELD, password)
        self.click_with_js(AccountPageLocators.LOGIN_BUTTON)
        self.is_element_visible(AccountPageLocators.LOGIN_AFTER_LOGOUT)
