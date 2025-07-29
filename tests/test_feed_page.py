import allure
import time
from curl import LOGIN_SITE
from pages.feed_page import OrderFeedPage
from pages.main_page import MainPage
from pages.profile_page import AccountPage
from data import EMAIL, PASSWORD

@allure.story('Раздел «Лента заказов»')
class TestOrderPage:
    @allure.title('Увеличения счётчика заказов «Выполнено за всё время»')
    def test_orders_all_time(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Получаем начальное значение счетчика'):
            order_feed_page.open_feed_page()
            initial_count = order_feed_page.get_total_orders_counter()

        with allure.step('Авторизируемся и создаем новый заказ'):
            driver.get(LOGIN_SITE)
            account_page.login(EMAIL, PASSWORD)
            time.sleep(2)

            main_page.drag_and_drop_ingr()
            main_page.click_place_order()
            time.sleep(3)

            order_feed_page.id_order_details()
            order_feed_page.click_close_details()
            time.sleep(2)

        with allure.step('Проверяем увеличение счетчика'):
            order_feed_page.open_feed_page()
            time.sleep(3)
            updated_count = order_feed_page.get_total_orders_counter()
            assert updated_count > initial_count, \
                f"Счетчик не увеличился. Был: {initial_count}, стал: {updated_count}"

    @allure.title('Увеличения счётчика заказов «Выполнено за сегодня»')
    def test_orders_today(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Получаем начальное значение счетчика за сегодня'):
            order_feed_page.open_feed_page()
            initial_today_count = order_feed_page.get_today_completed_counter()

        with allure.step('Авторизируемся и создаем новый заказ'):
            driver.get(LOGIN_SITE)
            account_page.login(EMAIL, PASSWORD)
            time.sleep(2)

            main_page.drag_and_drop_ingr()
            main_page.click_place_order()
            time.sleep(3)

            order_feed_page.id_order_details()
            order_feed_page.click_close_details()
            time.sleep(2)

        with allure.step('Проверяем увеличение счетчика за сегодня'):
            order_feed_page.open_feed_page()
            time.sleep(3)
            updated_today_count = order_feed_page.get_today_completed_counter()
            assert updated_today_count > initial_today_count, \
                f"Счетчик за сегодня не увеличился. Был: {initial_today_count}, стал: {updated_today_count}"

    @allure.title('Отображения номера заказа «В работе»')
    def test_order_in_work(self, driver):
        order_feed_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Вход в профиль'):
            driver.get(LOGIN_SITE)
            account_page.login(EMAIL, PASSWORD)
            time.sleep(2)

        with allure.step('Создаем новый заказ'):
            main_page.drag_and_drop_ingr()
            main_page.click_place_order()
            time.sleep(3)

        with allure.step('Получаем ID заказа'):
            order_id = order_feed_page.id_order_details()
            allure.attach(f"Создан заказ с ID: {order_id}", name="Order ID")
            time.sleep(2)

        with allure.step('Проверяем отображение заказа "В работе"'):
            order_feed_page.open_feed_page()
            time.sleep(3)
            assert order_feed_page.is_order_in_progress(order_id), \
                f"Заказ {order_id} не найден в разделе 'В работе'"
