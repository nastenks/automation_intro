from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.XPATH, "//button[@type='submit']")
    
    def login(self, email, password):
        self.find(self.USERNAME).send_keys(email)
        self.find(self.PASSWORD).send_keys(password)
        self.click(self.SUBMIT)