from src.pages.base_page import BasePage
from utils.locators import MainPageLocators

class MainPage(BasePage):
    def accept_cookies(self):
        """Принимает куки, если баннер отображается"""
        try:
            self.click(MainPageLocators.COOKIE_ACCEPT_BUTTON)
        except:
            pass  # Баннер может не отображаться
    
    def open_login_modal(self):
        """Открывает модальное окно входа"""
        self.is_visible(MainPageLocators.LOGIN_BUTTON)  # Сначала проверяем видимость
        self.click(MainPageLocators.LOGIN_BUTTON)
