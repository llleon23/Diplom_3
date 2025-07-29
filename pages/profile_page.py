from selenium.webdriver.common.by import By
from .base_page import BasePage
from locators.profile_locators import AccountPageLocators

class AccountPage(BasePage):
    def click_profile_button(self):
        self.click_when_clickable(AccountPageLocators.PROFILE_BUTTON)

    def click_order_history_button(self):
        self.click_to_element(AccountPageLocators.ORDER_HISTORY_BUTTON)

    def click_logout_button(self):
        self.click_to_element(AccountPageLocators.LOGOUT_BUTTON)

    def is_logout_button_visible(self):
        return self.is_element_visible(AccountPageLocators.LOGOUT_BUTTON)

    def is_order_completed(self):
        return self.get_text_from_element(AccountPageLocators.ORDER_COMPLETED) == "Выполнен"

    def is_login_button_visible_after_logout(self):
        return self.get_text_from_element(AccountPageLocators.LOGIN_AFTER_LOGOUT) == "Вход"

    def login(self, email, password):
        self.add_text_to_element(AccountPageLocators.EMAIL_FIELD, email)
        self.add_text_to_element(AccountPageLocators.PASSWORD_FIELD, password)
        self.click_with_js(AccountPageLocators.LOGIN_BUTTON)
        self.wait_for_element_visible(AccountPageLocators.LOGIN_AFTER_LOGOUT)

    def is_order_in_progress(self, order_id):
        try:
            clean_id = ''.join(filter(str.isdigit, order_id))
            formatted_id = f"{int(clean_id):07d}"

            order_in_progress_locator = (
                By.XPATH,
                f"//div[contains(@class, 'OrderFeed_orderListReady')]//p[contains(text(), '{formatted_id}')]"
            )

            return self.is_element_visible(order_in_progress_locator)
        except:
            return False
