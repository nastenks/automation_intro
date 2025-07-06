from pages.login_page import LoginPage
from src.pages.base_page import BasePage

def test_login():
    LoginPage(driver).login("test@example.com", "password123")
    assert MainPage(driver).is_welcome_message_displayed()

