from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click_to_element(self, locator, timeout=25):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def add_text_to_element(self, locator, text, timeout=5):
        self.find_element_with_wait(locator, timeout).send_keys(text)

    def get_text_from_element(self, locator, timeout=5):
        return self.find_element_with_wait(locator, timeout).text

    def scroll_to_element(self, locator, timeout=5):
        element = self.find_element_with_wait(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_when_clickable(self, locator, timeout=25):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def is_element_visible(self, locator, timeout=25):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def click_with_js(self, locator, timeout=25):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_element_visible(self, locator, timeout=15):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

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

    def is_element_displayed(self, locator, timeout=5):
        try:
            element = self.find_element_with_wait(locator, timeout)
            return element.is_displayed()
        except TimeoutException:
            return False

    def navigate_to(self, url):
        self.driver.get(url)

    def wait_until_condition(self, condition, timeout=30):
        WebDriverWait(self.driver, timeout).until(condition)

    def get_element_attribute(self, locator, attribute_name, timeout=5):
        element = self.find_element_with_wait(locator, timeout)
        return element.get_attribute(attribute_name)
