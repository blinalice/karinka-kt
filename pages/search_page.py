from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".product-thumb, .product-layout")
    PRODUCT_LINKS = (By.CSS_SELECTOR, ".product-thumb h4 a, .product-layout h4 a")
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#button-search, input[value='Search'], button[type='button'].btn")
    CONTENT = (By.ID, "content")

    def open_with_query(self, query):
        return self.open(f"index.php?route=product/search&search={query}")

    def products(self):
        if not self.is_visible(self.CONTENT):
            return []
        return self.driver.find_elements(*self.PRODUCT_CARDS)

    def open_first_product(self):
        self.clickable(self.PRODUCT_LINKS).click()
        return self

    def content_text(self):
        return self.visible(self.CONTENT).text
