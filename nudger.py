from selenium import webdriver

class google_nudger():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def search(self):
        self.driver.get("https://google.com")

    