from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Найти элемент с ожиданием")
    def find_element_with_wait(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Кликнуть по элементу")
    def click_to_element(self, locator, timeout=25):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step("Ввести текст")
    def add_text_to_element(self, locator, text, timeout=5):
        self.find_element_with_wait(locator, timeout).send_keys(text)

    @allure.step("Получить текст из элемента")
    def get_text_from_element(self, locator, timeout=5):
        return self.find_element_with_wait(locator, timeout).text

    @allure.step("Кликнуть по элементу, когда он станет кликабельным")
    def click_when_clickable(self, locator, timeout=25):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    @allure.step("Проверить видимость элемента")
    def is_element_visible(self, locator, timeout=25):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    @allure.step("Кликнуть по элементу с помощью JS")
    def click_with_js(self, locator, timeout=25):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Перетащить элемент на элемент")
    def drag_and_drop(self, source_locator, target_locator, timeout=5):
        element_from = self.find_element_with_wait(source_locator, timeout)
        element_to = self.find_element_with_wait(target_locator, timeout)
        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];
            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)

    @allure.step("Перейти по URL")
    def navigate_to(self, url):
        self.driver.get(url)

    @allure.step("Ожидать выполнения условия")
    def wait_until_condition(self, condition, timeout=15):
        WebDriverWait(self.driver, timeout).until(condition)

    @allure.step("Получить текст элемента")
    def get_element_text_or_default(self, locator, default="0000000"):
        try:
            element = self.find_element_with_wait(locator)
            order_text = element.text
            return ''.join(filter(str.isdigit, order_text)) or default
        except:
            return default

    @allure.step("Проверить наличие элемента на странице")
    def is_element_present(self, locator):
        try:
            element = self.find_element_with_wait(locator)
            return element is not None
        except:
            return False