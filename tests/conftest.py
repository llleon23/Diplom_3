import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from curl import MAIN_SITE
from data import EMAIL, PASSWORD


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Выбор браузера: 'chrome' или 'firefox'")


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()

    driver.get(MAIN_SITE)
    WebDriverWait(driver, 15).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    yield driver
    driver.quit()


@pytest.fixture
def authorized_driver(driver):
    from pages.profile_page import AccountPage  # Локальный импорт для избежания циклических зависимостей

    account_page = AccountPage(driver)
    account_page.login(EMAIL, PASSWORD)
    yield driver
