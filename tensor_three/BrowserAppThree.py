import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LocatorsThree import Locator

class BrowserToolsInit:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.base_url = Locator.base_url
        self.start_listdir = os.listdir()
        self.end_list = []

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
                    EC.presence_of_element_located(locator)
                )

    def start_site(self):
        return self.driver.get(self.base_url)