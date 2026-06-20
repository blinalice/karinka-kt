from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    LOGO = (By.CSS_SELECTOR, "#logo a, #logo img")
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button, button[type='button'].btn")
    PRODUCT_LINKS = (By.CSS_SELECTOR, ".product-thumb h4 a, .product-layout h4 a")
    MENU = (By.CSS_SELECTOR, "#menu, nav")
    FOOTER = (By.TAG_NAME, "footer")

    def open(self):
        return super().open("")

    def is_loaded(self):
        return self.is_visible(self.LOGO) and self.is_visible(self.SEARCH_INPUT)

    def search(self, query):
        self.type(self.SEARCH_INPUT, query)
        self.click(self.SEARCH_BUTTON)
        return self

    def first_product_link(self):
        return self.clickable(self.PRODUCT_LINKS)

    def menu_text(self):
        return self.visible(self.MENU).text

    def footer_text(self):
        self.scroll_to(self.FOOTER)
        return self.visible(self.FOOTER).text
