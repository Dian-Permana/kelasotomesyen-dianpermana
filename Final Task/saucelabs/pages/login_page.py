from selenium.webdriver.common.by import By
from locators.login import LocLogin

class Login:
    def __init__(self,driver):
        self.driver = driver

    def input_username(self,username):
        self.driver.find_element(By.ID,LocLogin.username_input).send_keys(username)

    def input_password(self,password):
        self.driver.find_element(By.ID,LocLogin.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.ID,LocLogin.login_button).click()
     
    def check_notifikasi(self):
        self.driver.find_element(By.XPATH,'//h3[@data-test="error"]').is_displayed()
        return True

    def text_notifikasi(self):
        text = self.driver.find_element(By.XPATH,'//h3[@data-test="error"]').text
        return text