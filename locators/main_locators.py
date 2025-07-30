from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCT_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[contains(text(),'Лента Заказов')]")
    INGR_R2D3_BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    INGR_DETAILS = (By.XPATH, "//h2[@class='Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10']")
    BURGER_SECTOR = (By.XPATH, "//section[@class='BurgerIngredients_ingredients__1N8v2']")
    CLOSE_INGR_DETAILS_BUTTON = (By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']//button[@type='button']//*[name()='svg']//*[name()='path' and contains(@fill-rule,'evenodd')]")
    ORDER_TARGET_TOP = (By.XPATH, "//img[@alt='Перетяните булочку сюда (верх)']")
    INGR_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']")
    COMPLETED_ORDERS = (By.XPATH, "//p[contains(@class, 'OrderFeed_number__2MbrQ')]")
