from BrowserAppOne import BrowserToolsInit
from LocatorsOne import Locator

class Navigation(BrowserToolsInit):
    def click_contact(self):
        return self.find_element(Locator.contact).click()

    def click_banner(self):
        self.find_element(Locator.banner).click()
        for window_handle in self.driver.window_handles:
            if window_handle != self.driver.current_window_handle:
                self.driver.close()
                self.driver.switch_to.window(window_handle)
                break

    def check_banner(self):
        if self.find_element(Locator.check_banner):
            return True
        else:
            return False

    def check_title(self):
        return self.driver.current_url == Locator.tensor_url

    def get_tensor(self):
        return self.find_element(Locator.tensor_about).click()

    def check_image(self):
        image_list = self.find_elements(Locator.list_image)
        image = set([(image.get_attribute("width"), image.get_attribute("height")) for image in image_list])
        return len(image) == 1