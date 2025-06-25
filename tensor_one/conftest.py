import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver
    chrome_driver.quit()