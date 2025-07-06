# фикстуры pytest
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config import Config

# @pytest.fixture(scope="session")
# def env_settings():
#     # return EnvironmentConfig().get_env_settings(config.ENVIRONMENT)
#     pass

# @pytest.fixture
# def browser(env_settings):
#     driver = webdriver.Chrome()
#     driver.get(env_settings["base_url"])
#     yield driver
#     driver.quit()

# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # Хук для скриншотов при падениях
#     pass

# @pytest.fixture
# def login_page(driver):
#     from pages.login_modal import LoginPage
#     return LoginPage(driver)


@pytest.fixture(scope="function")
def browser():
    # Настройка драйвера
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Для запуска в headless режиме
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def main_page(browser):
    from src.pages.main_page import MainPage
    browser.get(Config.DEV_URL)
    return MainPage(browser)