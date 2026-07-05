from playwright.sync_api import expect

from pages.inventory_page import InventoryPage


def test_inventory_page_title(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    expect(inventory_page.get_page_title()).to_have_text("Products")


def test_inventory_page_url(authenticated_page):
    assert "inventory" in authenticated_page.url

def test_page_heading(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    heading = inventory_page.get_inventory_page_heading()

    assert "Products" == heading

def test_add_to_cart_button(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.add_to_cart()
    button_text = inventory_page.get_remove_button_text()

    assert button_text == "Remove"

def test_remove_button(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.add_to_cart()
    inventory_page.remove_from_cart()
    button_text = inventory_page.get_add_button_text()

    assert button_text == "Add to cart"

def test_cart_icon_badge(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.add_to_cart()
    cart_count = inventory_page.get_cart_count()

    assert cart_count == "1"

def test_logout(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.open_menu()
    inventory_page.logout_account()

    assert "Swag Labs" == authenticated_page.title()

def test_sort_products_by_price_low_to_high(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.sort_products("lohi")
    product_prices = inventory_page.get_product_prices()

    assert product_prices == sorted(product_prices)

def test_sort_products_by_price_high_to_low(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.sort_products("hilo")
    product_prices = inventory_page.get_product_prices()

    assert product_prices == sorted(product_prices, reverse=True)

def test_sort_products_by_name_A_Z(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.sort_products("az")
    product_names = inventory_page.get_product_names()

    assert product_names == sorted(product_names)

def test_sort_products_by_name_Z_A(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.sort_products("za")
    product_names = inventory_page.get_product_names()

    assert product_names == sorted(product_names, reverse=True)
