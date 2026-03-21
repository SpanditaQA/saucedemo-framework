from pytest_bdd import given, when, then, parsers
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@given("user is logged in")
def login(browser):
    LoginPage(browser).login("standard_user", "secret_sauce")

@then("user should see products on the page")
def verify_products(browser):
    count = InventoryPage(browser).get_product_count()
    assert count > 0

@then("user should see 6 products")
def verify_product_count(browser):
    count = InventoryPage(browser).get_product_count()
    assert count == 6

@when(parsers.parse('user sorts products by "{order}"'))
def sort_products(browser, order):
    InventoryPage(browser).sort_products(order)

@then("products should be sorted successfully")
def verify_sort(browser):
    name = InventoryPage(browser).get_first_product_name()
    assert len(name) > 0

@when("user adds first product to cart")
def add_to_cart(browser):
    InventoryPage(browser).add_first_product_to_cart()

@then(parsers.parse('cart badge should show "{count}"'))
def verify_cart_badge(browser, count):
    assert InventoryPage(browser).get_cart_count() == count