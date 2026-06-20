from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RegisterPage(BasePage):
    FIRSTNAME = (By.ID, "input-firstname")
    LASTNAME = (By.ID, "input-lastname")
    EMAIL = (By.ID, "input-email")
    PASSWORD = (By.ID, "input-password")
    CONTENT = (By.ID, "content")

    def open(self):
        return super().open("index.php?route=account/register")

    def required_fields_are_visible(self):
        return all(self.is_visible(locator) for locator in [self.FIRSTNAME, self.LASTNAME, self.EMAIL, self.PASSWORD])
