from urllib.parse import urljoin

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, base_url, timeout=10):
        self.driver = driver
        self.base_url = base_url.rstrip("/") + "/"
        self.wait = WebDriverWait(driver, timeout)

    def open(self, path=""):
        self.driver.get(urljoin(self.base_url, path.lstrip("/")))
        return self

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def all_present(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.clickable(locator).click()
        return self

    def type(self, locator, text, clear=True):
        element = self.visible(locator)
        if clear:
            element.clear()
        element.send_keys(text)
        return self

    def text_of_page(self):
        return self.visible((By.TAG_NAME, "body")).text

    def is_visible(self, locator, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def scroll_to(self, locator):
        element = self.present(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element
