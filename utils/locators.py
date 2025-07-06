from selenium.webdriver.common.by import By

class MainPageLocators:
    COOKIE_BANNER = (By.CSS_SELECTOR, "app-cookie-consent.cookie-consent")
    COOKIE_ACCEPT_BUTTON = (By.CSS_SELECTOR, "button[data-translate-id='firebase-ru/COOKIE_CONSENT/BUTTON']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(., 'Войти')]")

class LoginModalLocators:
    MODAL = (By.CSS_SELECTOR, "app-sign")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input.regular-16.input.ng-tns-c1352732487-15")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input.regular-16.input.ng-tns-c1352732487-16[type='password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "app-button.sign-button button.afi-button")
