from selenium.webdriver.common.by import By

class Locator:
    base_url = "https://saby.ru"
    contact = (By.LINK_TEXT, "Контакты")
    banner = (By.XPATH, "//img[@alt='Разработчик системы Saby — компания «Тензор»']")
    check_banner = (By.XPATH, "//p[text()='Сила в людях']")
    tensor_url = "https://tensor.ru/about"
    tensor_about = (By.XPATH, '//a[@href="/about"]')
    list_image = (By.XPATH, '//div[@class="tensor_ru-container tensor_ru-section tensor_ru-About__block3"]//img')