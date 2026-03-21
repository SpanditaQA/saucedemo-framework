import pytest
from pages.login_page import LoginPage
from utils.excel_reader import read_login_data
from utils.logger import get_logger

logger = get_logger("ExcelDrivenTest")

# Read Excel once when file loads
login_data = read_login_data()

# Separate into pass and fail cases
pass_cases = [
    (r["username"], r["password"])
    for r in login_data
    if r["expected_result"] == "pass"
]

fail_cases = [
    (r["username"], r["password"])
    for r in login_data
    if r["expected_result"] == "fail"
]


# ✅ Valid users should reach inventory page
@pytest.mark.parametrize("username, password", pass_cases)
def test_valid_login_excel(browser, username, password):
    logger.info(f"VALID login test — user: {username}")
    LoginPage(browser).login(username, password)
    assert "inventory" in browser.current_url
    logger.info(f"✅ PASSED — {username} logged in successfully")


# ❌ Invalid users should NOT reach inventory page
@pytest.mark.parametrize("username, password", fail_cases)
def test_invalid_login_excel(browser, username, password):
    logger.info(f"INVALID login test — user: {username}")
    LoginPage(browser).login(username, password)
    assert "inventory" not in browser.current_url
    logger.info(f"✅ PASSED — {username} correctly rejected")
