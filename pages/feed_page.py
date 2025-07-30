import allure
import curl
from .base_page import BasePage
from locators.feed_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    @allure.step("Кликнуть на последний заказ")
    def click_last_order(self):
        self.click_to_element(OrderFeedPageLocators.LAST_ORDER)

    @allure.step("Получить счетчик общего количества заказов")
    def get_total_orders_counter(self):
        counter_text = self.get_text_from_element(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER)
        return int(counter_text) if counter_text else 0

    @allure.step("Получить счетчик выполненных сегодня заказов")
    def get_today_completed_counter(self):
        element = self.find_element_with_wait(OrderFeedPageLocators.TODAY_COMPLETED_COUNTER)
        return int(element.text.strip()) if element.text.strip().isdigit() else 0

    @allure.step("Открыть страницу ленты заказов")
    def open_feed_page(self):
        self.navigate_to(curl.FEED_SITE)
        self.is_element_visible(OrderFeedPageLocators.FEED_TITLE)

    @allure.step("Закрыть детали заказа")
    def click_close_details(self):
        self.click_with_js(OrderFeedPageLocators.CLOSE_DETAILS_BUTTON, timeout=15)

    @allure.step("Получить ID заказа из деталей")
    def id_order_details(self):
        return self.get_element_text_or_default(OrderFeedPageLocators.ORDER_ID)

    @allure.step("Проверить, что заказ в процессе выполнения")
    def is_order_in_progress(self, order_id):
        clean_id = ''.join(filter(str.isdigit, order_id))
        formatted_id = f"{int(clean_id):07d}"

        in_progress_locator = (
            OrderFeedPageLocators.ORDER_IN_PROGRESS[0],
            OrderFeedPageLocators.ORDER_IN_PROGRESS[1].format(formatted_id)
        )

        return self.is_element_present(in_progress_locator)
