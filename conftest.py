import pytest
import os
import time
import sys

# Fix path for parallel execution
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR)

from utils.driver_factory import get_driver
from utils.config_reader import read_config
from utils.logger import get_logger

logger = get_logger("conftest")

def pytest_configure(config):
    os.makedirs("reports", exist_ok=True)
    os.makedirs("reports/screenshots", exist_ok=True)
    os.makedirs("logs", exist_ok=True)

@pytest.fixture(scope="function")
def browser():
    config = read_config()
    driver = get_driver()
    driver.implicitly_wait(10)
    driver.get(config["url"])
    logger.info("Browser opened and navigated to SauceDemo")
    yield driver
    if not os.environ.get("CI"):
        time.sleep(2)
    driver.quit()
    logger.info("Browser closed")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    if result.when == "call" and result.failed:
        driver = item.funcargs.get("browser")
        if driver:
            os.makedirs("reports/screenshots", exist_ok=True)
            screenshot_path = f"reports/screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            logger.error(f"Test FAILED. Screenshot: {screenshot_path}")