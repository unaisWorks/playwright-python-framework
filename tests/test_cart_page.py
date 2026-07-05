from pages.inventory_page import InventoryPage

def test_cart_page_title(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    cart_page = inventory_page.click_cart_icon()
    page_title = cart_page.get_page_title()

    assert page_title == "Your Cart"

def test_continue_shopping_button(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()
    cart_page.continue_shopping()
    page_title = inventory_page.get_page_title()

    assert page_title == "Swag Labs"

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
    title_check = address_page.get_title()

    assert title_check == "Checkout: Your Information"
