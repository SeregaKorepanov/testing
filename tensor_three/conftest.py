import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromOption

@pytest.fixture(scope="session")
def browser():
    chrome_option = chromOption()
    chrome_option.add_experimental_option("prefs", {
        "download.default_directory": os.getcwd(),
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    chrome_driver = webdriver.Chrome(options=chrome_option)
    yield chrome_driver
    chrome_driver.quit()