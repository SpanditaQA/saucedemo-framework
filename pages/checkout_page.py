from selenium.webdriver.common.by import By

class CheckoutPage:

    first_name    = (By.ID, "first-name")
    last_name     = (By.ID, "last-name")
    postal_code   = (By.ID, "postal-code")
    continue_btn  = (By.ID, "continue")
    finish_btn    = (By.ID, "finish")
    cancel_btn    = (By.ID, "cancel")
    success_msg   = (By.CLASS_NAME, "complete-header")
    error_msg     = (By.CSS_SELECTOR, "[data-test='error']")

    def __init__(self, driver):
        self.driver = driver

    def enter_details(self, fname, lname, zip_code):
        self.driver.find_element(*self.first_name).send_keys(fname)
        self.driver.find_element(*self.last_name).send_keys(lname)
        self.driver.find_element(*self.postal_code).send_keys(zip_code)

    def click_continue(self):
        self.driver.find_element(*self.continue_btn).click()

    def click_finish(self):
        self.driver.find_element(*self.finish_btn).click()

    def click_cancel(self):
        self.driver.find_element(*self.cancel_btn).click()

    def get_success_message(self):
        return self.driver.find_element(*self.success_msg).text

    def get_error_message(self):
        return self.driver.find_element(*self.error_msg).text