from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Locators
    USERNAME_FIELD = (By.CLASS_NAME, "oxd-input")  
    PASSWORD_FIELD = (By.CLASS_NAME, "oxd-input")  
    LOGIN_BUTTON = (By.CLASS_NAME, "oxd-button")    

    def enter_username(self, username):
        username_input = self.driver.find_elements(*self.USERNAME_FIELD)[0]  
        username_input.send_keys(username)

    def enter_password(self, password):
        password_input = self.driver.find_elements(*self.PASSWORD_FIELD)[1]  
        password_input.send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        
     # Assertion: Verify that login was successful
        assert "dashboard" in self.driver.current_url, "Login failed!"
        print("Assertion passed. Login successful and dashboard loaded.")
