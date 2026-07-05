from playwright.sync_api import expect

from pages.inventory_page import InventoryPage
from data.address import FIRST_NAME, LAST_NAME, ZIP_CODE

def test_title_of_page(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()
    address_page = cart_page.continue_to_checkout()
    address_page.fill_address_form(FIRST_NAME , LAST_NAME , ZIP_CODE)
    overview_page  = address_page.proceed_to_overview_page()

    expect(overview_page.get_title()).to_have_text("Checkout: Overview")

def test_confirm_product_data(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()
    added_product = cart_page.get_added_item()
    address_page = cart_page.continue_to_checkout()
    address_page.fill_address_form(FIRST_NAME, LAST_NAME, ZIP_CODE)
    overview_page = address_page.proceed_to_overview_page()
    products = overview_page.fetch_products_name()

    assert products == added_product

def test_cancel_order(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()
    address_page = cart_page.continue_to_checkout()
    address_page.fill_address_form(FIRST_NAME, LAST_NAME, ZIP_CODE)
    overview_page = address_page.proceed_to_overview_page()
    inventory_page = overview_page.cancel_order()

    expect(inventory_page.get_page_title()).to_have_text("Products")

def test_finish_order(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()
    address_page = cart_page.continue_to_checkout()
    address_page.fill_address_form(FIRST_NAME, LAST_NAME, ZIP_CODE)
    overview_page = address_page.proceed_to_overview_page()
    success_page = overview_page.finish_order()

    expect(success_page.get_title()).to_have_text("Checkout: Complete!")



