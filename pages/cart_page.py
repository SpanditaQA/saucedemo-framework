from selenium.webdriver.common.by import By

class CartPage:

    cart_icon       = (By.CLASS_NAME, "shopping_cart_link")
    cart_items      = (By.CLASS_NAME, "cart_item")
    remove_btn      = (By.CSS_SELECTOR, "button[data-test^='remove']")
    continue_btn    = (By.ID, "continue-shopping")
    checkout_btn    = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver

    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()

    def get_cart_item_count(self):
        return len(self.driver.find_elements(*self.cart_items))

    def remove_first_item(self):
        self.driver.find_elements(*self.remove_btn)[0].click()

    def click_continue_shopping(self):
        self.driver.find_element(*self.continue_btn).click()

    def click_checkout(self):
        self.driver.find_element(*self.checkout_btn).click()