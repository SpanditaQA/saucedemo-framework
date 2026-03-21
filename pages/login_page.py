from selenium.webdriver.common.by import By
from utils.logger import get_logger

logger = get_logger("LoginPage")

class LoginPage:

    username  = (By.ID, "user-name")
    password  = (By.ID, "password")
    login_btn = (By.ID, "login-button")
    error_msg = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        logger.info("Opening SauceDemo login page")
        self.driver.get("https://www.saucedemo.com/")

    def login(self, user, pwd):
        logger.info(f"Logging in with user: {user}")
        self.driver.find_element(*self.username).send_keys(user)
        self.driver.find_element(*self.password).send_keys(pwd)
        self.driver.find_element(*self.login_btn).click()

    def get_error_message(self):
        msg = self.driver.find_element(*self.error_msg).text
        logger.info(f"Error message found: {msg}")
        return msg