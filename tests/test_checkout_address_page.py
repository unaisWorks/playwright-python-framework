from playwright.sync_api import expect

from pages.inventory_page import InventoryPage
from data.address import FIRST_NAME, LAST_NAME, ZIP_CODE

def test_title(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()
    address_page = cart_page.continue_to_checkout()

    expect(address_page.get_title()).to_have_text("Checkout: Your Information")

def test_address_flow(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()
    address_page = cart_page.continue_to_checkout()
    address_page.fill_address_form(FIRST_NAME, LAST_NAME, ZIP_CODE)
    overview_page = address_page.proceed_to_overview_page()

    expect(overview_page.get_title()).to_have_text("Checkout: Overview")

