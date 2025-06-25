from BrowserAppTwo import BrowserToolsInit
from LocatorsTwo import Locator

class ChangeRegion(BrowserToolsInit):
    def click_contact(self):
        return self.find_element(Locator.contact).click()

    def check_region(self):
        region = self.find_element(Locator.get_region)
        self.list_partners = self.find_elements(Locator.list_partners)
        return region != ""

    def check_partners_start(self):
        self.list_partners = self.find_elements(Locator.list_partners)
        return len(self.list_partners) != 0

    def set_region(self):
        self.find_element(Locator.get_region).click()
        self.find_element(Locator.set_region).click()
        self.wait_title(Locator.new_title)

    def check_new_title(self):
        return Locator.new_check_title in self.driver.title

    def check_new_url(self):
        return Locator.new_url in self.driver.current_url

    def check_new_region(self):
        return Locator.new_check_title in self.find_element(Locator.get_region).text

    def check_new_partners(self):
        partners = self.find_elements(Locator.list_partners)
        return len(self.list_partners) != len(partners)