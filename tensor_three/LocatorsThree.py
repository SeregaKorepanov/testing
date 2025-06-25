from selenium.webdriver.common.by import By

class Locator:
    base_url = "https://saby.ru"
    loading_local = (By.XPATH, '//a[text()="Скачать локальные версии"]')
    desktop = (By.XPATH, '//div[@data-id="plugin"]')
    load_file = (By.PARTIAL_LINK_TEXT, 'Exe')