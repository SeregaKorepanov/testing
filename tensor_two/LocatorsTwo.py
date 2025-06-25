from selenium.webdriver.common.by import By

class Locator:
    base_url = "https://saby.ru"
    contact = (By.LINK_TEXT, "Контакты")
    get_region = (By.XPATH, '//span[@class="sbis_ru-Region-Chooser__text sbis_ru-link"]')
    list_partners = (By.XPATH, '//div[@class="sbisru-Contacts-List__col-1"]')
    set_region = (By.XPATH, '//span[@title="Камчатский край"]')
    new_title = "Saby Контакты — Камчатский край"
    new_url = "kamchatskij"
    new_check_title = "Камчатский"

