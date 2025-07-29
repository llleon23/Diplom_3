from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from locators.feed_locators import OrderFeedPageLocators
import time


class OrderFeedPage(BasePage):
    def click_last_order(self):
        self.click_to_element(OrderFeedPageLocators.LAST_ORDER)

    def get_order_details_content(self):
        return self.get_text_from_element(OrderFeedPageLocators.ORDER_DETAILS_CONTENT)

    def get_total_orders_counter(self):
        counter_text = self.get_text_from_element(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER)
        return int(counter_text) if counter_text else 0

    def get_today_completed_counter(self):
        element = self.find_element_with_wait(OrderFeedPageLocators.TODAY_COMPLETED_COUNTER)
        return int(element.text.strip()) if element.text.strip().isdigit() else 0

    def open_feed_page(self):
        self.navigate_to("https://stellarburgers.nomoreparties.site/feed")
        self.wait_for_element_visible(OrderFeedPageLocators.FEED_TITLE)

    def click_construct(self):
        self.click_to_element(OrderFeedPageLocators.CONSTRUCT_BUTTON)

    def click_feed(self):
        self.click_when_clickable(OrderFeedPageLocators.ORDER_FEED_BUTTON)

    def click_place_order(self):
        self.click_to_element(OrderFeedPageLocators.PLACE_ORDER_BUTTON)

    def click_profile_button(self):
        self.click_when_clickable(OrderFeedPageLocators.PROFILE_BUTTON)

    def click_close_details(self):
        try:
            close_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable(OrderFeedPageLocators.CLOSE_DETAILS_BUTTON)
            )
            self.driver.execute_script("arguments[0].click();", close_button)
            time.sleep(1)
        except Exception as e:
            print(f"Failed to close order details: {str(e)}")
            raise

    def id_order_details(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(OrderFeedPageLocators.ORDER_ID)
            )
            order_text = self.get_text_from_element(OrderFeedPageLocators.ORDER_ID)
            return ''.join(filter(str.isdigit, order_text))
        except Exception as e:
            print(f"Failed to get order ID: {str(e)}")
            return "0000000"

    def id_in_feed(self, order_id):
        try:
            clean_id = ''.join(filter(str.isdigit, order_id))
            formatted_id = f"{int(clean_id):07d}"

            order_locator = (
                OrderFeedPageLocators.ORDER_ID_IN_FEED[0],
                OrderFeedPageLocators.ORDER_ID_IN_FEED[1].format(formatted_id)
            )

            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(order_locator)
            )
            return True
        except:
            return False

    def is_order_in_progress(self, order_id):
        try:
            clean_id = ''.join(filter(str.isdigit, order_id))
            formatted_id = f"{int(clean_id):07d}"

            in_progress_locator = (
                OrderFeedPageLocators.ORDER_IN_PROGRESS[0],
                OrderFeedPageLocators.ORDER_IN_PROGRESS[1].format(formatted_id)
            )

            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(in_progress_locator)
            )
            return True
        except:
            return False
