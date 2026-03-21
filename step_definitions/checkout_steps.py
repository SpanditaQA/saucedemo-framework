from pytest_bdd import given, when, then
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@given("user is logged in with item in cart and on checkout page")
def setup_checkout(browser):
    LoginPage(browser).login("standard_user", "secret_sauce")
    InventoryPage(browser).add_first_product_to_cart()
    CartPage(browser).go_to_cart()
    CartPage(browser).click_checkout()

@when("user fills valid checkout details")
def fill_valid_details(browser):
    CheckoutPage(browser).enter_details("John", "Doe", "12345")

@when("user fills checkout with missing first name")
def fill_missing_fname(browser):
    CheckoutPage(browser).enter_details("", "Doe", "12345")

@when("user fills checkout with missing last name")
def fill_missing_lname(browser):
    CheckoutPage(browser).enter_details("John", "", "12345")

@when("user fills checkout with missing postal code")
def fill_missing_zip(browser):
    CheckoutPage(browser).enter_details("John", "Doe", "")

@when("user clicks continue on checkout")
def click_continue(browser):
    CheckoutPage(browser).click_continue()

@when("user clicks finish")
def click_finish(browser):
    CheckoutPage(browser).click_finish()

@when("user cancels checkout")
def cancel_checkout(browser):
    CheckoutPage(browser).click_cancel()

@then("order should be placed successfully")
def verify_order(browser):
    msg = CheckoutPage(browser).get_success_message()
    assert "Thank you" in msg

@then("checkout error should be displayed")
def verify_checkout_error(browser):
    msg = CheckoutPage(browser).get_error_message()
    assert len(msg) > 0

@then("user should be back on cart page")
def verify_cart_page(browser):
    assert "cart" in browser.current_url