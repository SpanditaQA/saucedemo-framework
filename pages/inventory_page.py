from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class InventoryPage:

    product_list     = (By.CLASS_NAME, "inventory_item")
    sort_dropdown    = (By.CLASS_NAME, "product_sort_container")
    add_to_cart_btns = (By.CSS_SELECTOR, "button[data-test^='add-to-cart']")
    cart_badge       = (By.CLASS_NAME, "shopping_cart_badge")
    product_names    = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver

    def get_product_count(self):
        return len(self.driver.find_elements(*self.product_list))

    def sort_products(self, order):
        Select(self.driver.find_element(*self.sort_dropdown)).select_by_value(order)

    def get_first_product_name(self):
        return self.driver.find_elements(*self.product_names)[0].text

    def add_first_product_to_cart(self):
        self.driver.find_elements(*self.add_to_cart_btns)[0].click()

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_badge).text