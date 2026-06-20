from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    TITLE = (By.CSS_SELECTOR, "#content h1, h1")
    ADD_TO_CART = (By.ID, "button-cart")
    QUANTITY = (By.ID, "input-quantity")
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success, .alert-dismissible, #alert .alert")

    def title(self):
        return self.visible(self.TITLE).text

    def add_to_cart(self):
        self.scroll_to(self.ADD_TO_CART)
        self.click(self.ADD_TO_CART)
        return self

    def success_text(self):
        return self.visible(self.SUCCESS_ALERT).text

    def set_quantity(self, value):
        self.type(self.QUANTITY, str(value))
        return self

    def quantity_value(self):
        return self.visible(self.QUANTITY).get_attribute("value")
