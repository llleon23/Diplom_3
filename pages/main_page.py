from pages.base_page import BasePage
from locators.main_locators import MainPageLocators

class MainPage(BasePage):
    def click_construct(self):
        self.click_to_element(MainPageLocators.CONSTRUCT_BUTTON)
        self.wait_for_element_visible(MainPageLocators.BURGER_SECTOR)

    def click_place_order(self):
        self.click_to_element(MainPageLocators.PLACE_ORDER_BUTTON)

    def is_burger_sector_visible(self):
        return self.is_element_visible(MainPageLocators.BURGER_SECTOR)

    def click_order_feed(self):
        self.click_to_element(MainPageLocators.ORDER_FEED_BUTTON)
        self.wait_for_element_visible(MainPageLocators.COMPLETED_ORDERS, timeout=10)

    def is_order_feed_counter_visible(self):
        return self.is_element_visible(MainPageLocators.COMPLETED_ORDERS)

    def click_ingredient(self):
        self.click_to_element(MainPageLocators.INGR_R2D3_BUN)
        self.wait_for_element_visible(MainPageLocators.CLOSE_INGR_DETAILS_BUTTON)

    def is_ingr_details_visible(self):
        return self.is_element_visible(MainPageLocators.CLOSE_INGR_DETAILS_BUTTON)

    def close_ingr_details(self):
        self.click_to_element(MainPageLocators.CLOSE_INGR_DETAILS_BUTTON)

    def get_ingr_counter(self):
        counter_text = self.get_text_from_element(MainPageLocators.INGR_COUNTER)
        return int(counter_text) if counter_text else 0

    def drag_and_drop_ingr(self):
        self.drag_and_drop(
            MainPageLocators.INGR_R2D3_BUN,
            MainPageLocators.ORDER_TARGET_TOP
        )
        self.wait_until_condition(
            lambda d: self.get_ingr_counter() > 0
        )
