from pytest_bdd import given, when, then, parsers
from pages.login_page import LoginPage

@given("user is on login page")
def open_page(browser):
    pass  # browser already on page via conftest

@when("user logs in with valid credentials")
def login_valid(browser):
    LoginPage(browser).login("standard_user", "secret_sauce")

@when("user logs in with invalid credentials")
def login_invalid(browser):
    LoginPage(browser).login("wrong_user", "wrong_pass")

@when("user logs in with blank username")
def login_blank_username(browser):
    LoginPage(browser).login("", "secret_sauce")

@when("user logs in with blank password")
def login_blank_password(browser):
    LoginPage(browser).login("standard_user", "")

@when("locked out user tries to login")
def login_locked(browser):
    LoginPage(browser).login("locked_out_user", "secret_sauce")

@when(parsers.parse('user logs in as "{username}" with password "{password}"'))
def login_parametrized(browser, username, password):
    LoginPage(browser).login(username, password)

@then("user should land on inventory page")
def verify_login(browser):
    assert "inventory" in browser.current_url

@then("user should see error message")
def verify_error(browser):
    msg = LoginPage(browser).get_error_message()
    assert len(msg) > 0

@then("user should see locked error message")
def verify_locked(browser):
    msg = LoginPage(browser).get_error_message()
    assert "locked" in msg.lower()