from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from utils.locators import LoginModalLocators

class LoginModal(BasePage):
    def is_modal_visible(self):
        """Проверяет, что модальное окно отображается"""
        return self.is_visible(LoginModalLocators.MODAL)
    
    def login(self, email, password):
        """Выполняет вход с правильными ожиданиями"""
        # Ввод email с ожиданием доступности поля
        self.wait.until(EC.element_to_be_clickable(LoginModalLocators.EMAIL_INPUT))
        self.input_text(LoginModalLocators.EMAIL_INPUT, email)
        
        # Ввод пароля с проверкой, что поле стало активным
        self.wait.until(EC.element_to_be_clickable(LoginModalLocators.PASSWORD_INPUT))
        self.input_text(LoginModalLocators.PASSWORD_INPUT, password)
        
        # Ожидание кликабельности кнопки с дополнительными проверками
        submit_button = self.wait.until(
            lambda driver: driver.find_element(*LoginModalLocators.SUBMIT_BUTTON).is_enabled() and 
            driver.find_element(*LoginModalLocators.SUBMIT_BUTTON).is_displayed()
        )
        self.click(LoginModalLocators.SUBMIT_BUTTON)
        
        # Дополнительное ожидание после клика (если нужно)
        self.wait.until(
            EC.invisibility_of_element_located(LoginModalLocators.MODAL)
        )
        