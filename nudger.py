from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from eco_searches import climate_change

class google_nudger():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def search(self):
        for i in climate_change:
            sleep(1)
            self.driver.get("https://google.com")
            sleep(1)
            search_bar = self.driver.find_element_by_css_selector("[title^='Search']")
            search_bar.click()
            sleep(1)
            search_bar.send_keys(i)
            sleep(1)
            search_bar.send_keys(Keys.ENTER)
            # search_btn = self.driver.find_element_by_css_selector("[class^='gNO89b']")
            # search_btn.click()

