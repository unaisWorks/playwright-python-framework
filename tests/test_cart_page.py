from playwright.sync_api import expect

from pages.inventory_page import InventoryPage

def test_cart_page_title(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    cart_page = inventory_page.click_cart_icon()

    expect(cart_page.get_page_title()).to_have_text("Your Cart")

def test_continue_shopping_button(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()
    cart_page.continue_shopping()

    expect(inventory_page.get_page_title()).to_have_text("Products")


def test_item_appears_in_cart(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    added_items = inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()
    cart_items = cart_page.get_added_item_name()

    assert added_items == cart_items

def test_remove_button_on_cart(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()
    cart_page.remove_item_from_cart()
    cart_count = cart_page.is_cart_empty()

    assert cart_count == True

def test_checkout_button(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()
    address_page = cart_page.continue_to_checkout()

    expect(address_page.get_title()).to_have_text("Checkout: Your Information")

