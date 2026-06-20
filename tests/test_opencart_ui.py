import pytest
from pages.account_page import RegisterPage
from pages.contact_page import ContactPage
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.search_page import SearchPage


@pytest.mark.ui
def test_home_page_opened(browser, base_url):
    page = HomePage(browser, base_url).open()
    assert page.is_loaded()


@pytest.mark.ui
def test_header_search_input_accepts_text(browser, base_url):
    page = HomePage(browser, base_url).open()
    page.type(HomePage.SEARCH_INPUT, "MacBook")
    assert page.visible(HomePage.SEARCH_INPUT).get_attribute("value") == "MacBook"


@pytest.mark.ui
def test_search_existing_product_returns_results(browser, base_url):
    HomePage(browser, base_url).open().search("MacBook")
    page = SearchPage(browser, base_url)
    assert len(page.products()) > 0
    assert "macbook" in page.content_text().lower()


@pytest.mark.ui
def test_search_nonexistent_product_shows_empty_result(browser, base_url):
    page = SearchPage(browser, base_url).open_with_query("qwerty_product_12345")
    text = page.content_text().lower()
    assert len(page.products()) == 0
    assert "no product" in text or "нет товаров" in text or "there is no product" in text


@pytest.mark.ui
def test_product_card_opens_from_search(browser, base_url):
    SearchPage(browser, base_url).open_with_query("MacBook").open_first_product()
    page = ProductPage(browser, base_url)
    assert page.title() != ""
    assert page.is_visible(ProductPage.ADD_TO_CART)


@pytest.mark.ui
def test_product_quantity_field_accepts_value(browser, base_url):
    SearchPage(browser, base_url).open_with_query("MacBook").open_first_product()
    page = ProductPage(browser, base_url).set_quantity(2)
    assert page.quantity_value() == "2"


@pytest.mark.ui
def test_add_product_to_cart_shows_success_message(browser, base_url):
    SearchPage(browser, base_url).open_with_query("MacBook").open_first_product()
    page = ProductPage(browser, base_url).add_to_cart()
    text = page.success_text().lower()
    assert "success" in text or "shopping cart" in text or "корзин" in text


@pytest.mark.ui
def test_shopping_cart_page_available(browser, base_url):
    page = SearchPage(browser, base_url).open("index.php?route=checkout/cart")
    text = page.text_of_page().lower()
    assert "shopping cart" in text or "корзин" in text


@pytest.mark.ui
def test_contact_page_form_fields_are_present(browser, base_url):
    page = ContactPage(browser, base_url).open()
    assert page.fields_are_visible()


@pytest.mark.ui
def test_contact_form_validation_for_empty_submit(browser, base_url):
    page = ContactPage(browser, base_url).open().submit_empty()
    assert page.has_validation_error()


@pytest.mark.ui
def test_registration_page_form_fields_are_present(browser, base_url):
    page = RegisterPage(browser, base_url).open()
    assert page.required_fields_are_visible()
