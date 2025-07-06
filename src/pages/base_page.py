 # Page Object Model 
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    def find(self, locator):
        return self.driver.find_element(*locator)
        
    def click(self, locator):
        self.find(locator).click()