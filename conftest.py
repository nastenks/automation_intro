# фикстуры pytest
import pytest
from selenium import webdriver
import config

@pytest.fixture(scope="session")
def env_settings():
    # return EnvironmentConfig().get_env_settings(config.ENVIRONMENT)
    pass

@pytest.fixture
def browser(env_settings):
    driver = webdriver.Chrome()
    driver.get(env_settings["base_url"])
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Хук для скриншотов при падениях
    pass

@pytest.fixture
def login_page(driver):
    from src.pages.login_page import LoginPage
    return LoginPage(driver)