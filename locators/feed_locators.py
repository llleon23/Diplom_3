from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    CONSTRUCT_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    ORDER_DETAILS_CONTENT = (By.XPATH, "//p[@class='text text_type_main-medium mb-8']")
    CLOSE_DETAILS_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_')]")
    TODAY_COMPLETED_COUNTER = (By.XPATH, "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    ORDER_ID_IN_FEED = (By.XPATH, "//*[contains(text(), '{0}')]")
    ORDER_IN_PROGRESS = (By.CSS_SELECTOR, "ul.OrderFeed_orderList__cBvyi")
    FEED_TITLE = (By.XPATH, "//h1[contains(@class, 'text_type_main-large')]")
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    ORDER_ID = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title') and normalize-space(text())]")
    LAST_ORDER = (By.CSS_SELECTOR, "ul.OrderFeed_list li:first-child a div")
