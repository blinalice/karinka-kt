from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ContactPage(BasePage):
    NAME = (By.ID, "input-name")
    EMAIL = (By.ID, "input-email")
    ENQUIRY = (By.ID, "input-enquiry")
    SUBMIT = (By.CSS_SELECTOR, "input[type='submit'], button[type='submit']")
    CONTENT = (By.ID, "content")
    ERROR = (By.CSS_SELECTOR, ".text-danger, .invalid-feedback, .alert-danger")

    def open(self):
        return super().open("index.php?route=information/contact")

    def fields_are_visible(self):
        return all(self.is_visible(locator) for locator in [self.NAME, self.EMAIL, self.ENQUIRY])

    def submit_empty(self):
        self.scroll_to(self.SUBMIT)
        self.click(self.SUBMIT)
        return self

    def has_validation_error(self):
        return self.is_visible(self.ERROR, timeout=5)
