from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from eco_searches import climate_change
import secrets

class google_nudger():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions(); 
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']); 
        self.driver = webdriver.Chrome(options=chrome_options)
        # self.driver = webdriver.Firefox(executable_path=r'/Users/rohitmusti/geckodriver')

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
    
    def login(self):
        self.driver.get("https://google.com")
        sleep(1)
        login_btn = bot.driver.find_elements_by_xpath("//*[contains(text(), 'Sign in')]")
        login_btn[0].click()
        email_fld = bot.driver.find_element_by_css_selector("[type='email']")
        sleep(1)
        email_fld.click()
        sleep(1)
        email_fld.send_keys(Keys.ENTER)
        sleep(1)
        pass_fld = bot.driver.find_element_by_css_selector("[type='password']")
        pass_fld.click()
        sleep(1)
        pass_fld.send_keys(secrets.password)
        pass_fld.send_keys(Keys.ENTER)

    if __name__=='__main__':
        bot = google_nudger()
        bot.search()

