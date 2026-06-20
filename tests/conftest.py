import os
import re
from pathlib import Path

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

try:
    import allure
except Exception:
    allure = None


ROOT_DIR = Path(__file__).resolve().parents[1]
SCREENSHOTS_DIR = ROOT_DIR / "artifacts" / "screenshots"


def pytest_addoption(parser):
    parser.addoption("--base-url", action="store", default=os.getenv("BASE_URL", "http://localhost:8082"))
    parser.addoption("--headed", action="store_true", default=False)


@pytest.fixture(scope="session")
def base_url(pytestconfig):
    return pytestconfig.getoption("--base-url").rstrip("/")


@pytest.fixture
def browser(pytestconfig):
    options = Options()
    if not pytestconfig.getoption("--headed") and os.getenv("HEADLESS", "true").lower() in {"1", "true", "yes"}:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return
    driver = item.funcargs.get("browser")
    if driver is None:
        return
    SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
    safe_name = re.sub(r"[^a-zA-Z0-9_-]+", "_", item.name)
    screenshot_path = SCREENSHOTS_DIR / f"{safe_name}.png"
    driver.save_screenshot(str(screenshot_path))
    if allure is not None:
        allure.attach.file(str(screenshot_path), name=safe_name, attachment_type=allure.attachment_type.PNG)
