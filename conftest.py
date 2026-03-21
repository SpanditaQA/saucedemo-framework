import pytest
import os
import time
from utils.driver_factory import get_driver
from utils.config_reader import read_config
from utils.logger import get_logger

logger = get_logger("conftest")

@pytest.fixture
def browser():
    config = read_config()
    driver = get_driver()
    driver.implicitly_wait(10)
    driver.get(config["url"])
    logger.info("Browser opened and navigated to SauceDemo")
    yield driver
    time.sleep(3)       # pause before closing so you can see final state
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
            logger.error(f"Test FAILED. Screenshot saved: {screenshot_path}")