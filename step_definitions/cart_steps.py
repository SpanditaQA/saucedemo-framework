from pytest_bdd import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@given("user is logged in and item is added")
def login_and_add(browser):
    LoginPage(browser).login("standard_user", "secret_sauce")
    InventoryPage(browser).add_first_product_to_cart()

@when("user goes to cart")
def go_to_cart(browser):
    CartPage(browser).go_to_cart()

@then("cart page should load")
def verify_cart_page(browser):
    assert "cart" in browser.current_url

@then("cart should have 1 item")
def verify_cart_count(browser):
    assert CartPage(browser).get_cart_item_count() == 1

@when("user removes item from cart")
def remove_item(browser):
    CartPage(browser).remove_first_item()

@then("cart should be empty")
def verify_empty_cart(browser):
    assert CartPage(browser).get_cart_item_count() == 0

@when("user clicks continue shopping")
def continue_shopping(browser):
    CartPage(browser).click_continue_shopping()

@then("user should be back on inventory page")
def verify_inventory_page(browser):
    assert "inventory" in browser.current_url

@when("user clicks checkout")
def checkout(browser):
    CartPage(browser).click_checkout()

@then("user should be on checkout page")
def verify_checkout_page(browser):
    assert "checkout" in browser.current_url