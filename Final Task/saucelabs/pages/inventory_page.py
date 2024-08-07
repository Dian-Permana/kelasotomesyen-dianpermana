from selenium.webdriver.common.by import By
from locators.inventory import LocInventory

class Inventory:
    def __init__(self, driver):
        self.driver = driver
        
    def check_title(self):
        title = self.driver.find_element(By.XPATH,LocInventory.title_text).text
        return title