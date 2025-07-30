import allure
import data
from curl import LOGIN_SITE
from pages.main_page import MainPage
from pages.profile_page import AccountPage

@allure.feature('Основной функционал')
@allure.story('Тесты функционала главной страницы')
class TestMainPage:

    @allure.title('переход по клику на «Конструктор»')
    def test_construct(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Авторизируемся'):
            driver.get(LOGIN_SITE)
            account_page.login(data.EMAIL, data.PASSWORD)

        with allure.step('Нажимаем на кнопку "Конструктор"'):
            main_page.click_construct()

        with allure.step('Проверяем отображение секции конструктора'):
            assert main_page.is_burger_sector_visible(), "Конструктор не отображается"

    @allure.title('переход по клику на раздел «Лента заказов»')
    def test_feed(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Авторизация'):
            driver.get(LOGIN_SITE)
            account_page.login(data.EMAIL, data.PASSWORD)

        with allure.step('Нажимаем на кнопку "Лента заказов"'):
            main_page.click_order_feed()

        with allure.step('Проверяем отображение счетчика заказов'):
            assert main_page.is_order_feed_counter_visible(), "Счетчик заказов не отобразился"

    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_ingredient(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Авторизация'):
            driver.get(LOGIN_SITE)
            account_page.login(data.EMAIL, data.PASSWORD)

        with allure.step('Нажимаем на ингредиент'):
            main_page.click_ingredient()

        with allure.step('Проверяем отображение деталей'):
            assert main_page.is_ingr_details_visible(), "Детали ингредиента не отобразились"

    @allure.title('всплывающее окно закрывается кликом по крестику')
    def test_close(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Авторизация'):
            driver.get(LOGIN_SITE)
            account_page.login(data.EMAIL, data.PASSWORD)

        with allure.step('Открываем детали ингредиента'):
            main_page.click_ingredient()

        with allure.step('Закрываем детали'):
            main_page.close_ingr_details()

        with allure.step('Проверяем закрытие окна'):
            assert not main_page.is_ingr_details_visible(), "Окно деталей не закрылось"

    @allure.title('при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_ingredients(self, driver):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)

        with allure.step('Авторизация'):
            driver.get(LOGIN_SITE)
            account_page.login(data.EMAIL, data.PASSWORD)

        with allure.step('Получаем начальное значение счетчика'):
            initial_counter = main_page.get_ingr_counter()

        with allure.step('Добавляем ингредиент в заказ'):
            main_page.drag_and_drop_ingr()

        with allure.step('Проверяем увеличение счетчика'):
            updated_counter = main_page.get_ingr_counter()
            assert updated_counter > initial_counter, "Счетчик не увеличился"
