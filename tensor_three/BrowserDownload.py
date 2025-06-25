import os
from BrowserAppThree import BrowserToolsInit
from LocatorsThree import Locator
from time import sleep, time


class Loading(BrowserToolsInit):
    def click_local_load(self):
        return self.find_element(Locator.loading_local).click()

    def click_desktop(self):
        return self.find_element(Locator.desktop).click()

    def loading_file(self):
        self.find_element(Locator.load_file).click()
        time_end = 10
        start_time = time()
        self.end_list = []
        while time() - start_time < time_end:
            self.end_list = [file for file in os.listdir() if file not in self.start_listdir]
            if ".exe" in "".join(self.end_list):
                break
            else:
                sleep(0.5)

    def check_file(self):
        return ".exe" in "".join(self.end_list)

    def check_size_file(self):
        wait_size = float(self.find_element(Locator.load_file).text.split()[-2])
        actual_size = round(os.stat(self.end_list[0]).st_size/1024/1024, 2)
        return wait_size == actual_size