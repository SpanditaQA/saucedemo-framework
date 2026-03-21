import time
from pytest_bdd import given, when, then, parsers
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import get_logger

logger = get_logger("E2ETest")

STEP_DELAY = 1.5   # seconds between each step — change this to make faster/slower

@given("user opens the saucedemo website")
def open_website(browser):
    logger.info("E2E Test Started - SauceDemo opened")
    time.sleep(STEP_DELAY)

@when("user logs in with valid credentials")
def e2e_login(browser):
    logger.info("Logging in as standard_user")
    LoginPage(browser).login("standard_user", "secret_sauce")
    time.sleep(STEP_DELAY)

@then("user should land on inventory page")
def verify_inventory(browser):
    logger.info("Verifying inventory page loaded")
    assert "inventory" in browser.current_url
    time.sleep(STEP_DELAY)

@when("user sorts products by price low to high")
def sort_by_price(browser):
    logger.info("Sorting products: price low to high")
    InventoryPage(browser).sort_products("lohi")
    time.sleep(STEP_DELAY)

@when("user adds first product to cart")
def add_product(browser):
    name = InventoryPage(browser).get_first_product_name()
    logger.info(f"Adding product to cart: {name}")
    InventoryPage(browser).add_first_product_to_cart()
    time.sleep(STEP_DELAY)

@then(parsers.parse('cart badge should show count as "{count}"'))
def verify_badge(browser, count):
    logger.info(f"Verifying cart badge shows: {count}")
    assert InventoryPage(browser).get_cart_count() == count
    time.sleep(STEP_DELAY)

@when("user goes to the cart page")
def go_to_cart(browser):
    logger.info("Navigating to cart page")
    CartPage(browser).go_to_cart()
    time.sleep(STEP_DELAY)

@then("cart should contain 1 item")
def verify_cart_has_item(browser):
    logger.info("Verifying cart has 1 item")
    assert CartPage(browser).get_cart_item_count() == 1
    time.sleep(STEP_DELAY)

@when("user removes the item from cart")
def remove_from_cart(browser):
    logger.info("Removing item from cart")
    CartPage(browser).remove_first_item()
    time.sleep(STEP_DELAY)

@then("cart should be empty now")
def verify_cart_empty(browser):
    logger.info("Verifying cart is empty")
    assert CartPage(browser).get_cart_item_count() == 0
    logger.info("E2E Test COMPLETED successfully")
    time.sleep(STEP_DELAY)