from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from data.address import FIRST_NAME , LAST_NAME, ZIP_CODE

def test_title_of_page(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()

    address_page = cart_page.continue_to_checkout()
    address_page.fill_address_form(FIRST_NAME, LAST_NAME, ZIP_CODE)
    overview_page = address_page.proceed_to_overview_page()

    success_page = overview_page.finish_order()
    title = success_page.get_title()

    assert title == "Checkout: Complete!"

def test_success_message(authenticated_page):
    inventory_page = InventoryPage(authenticated_page)
    inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()

    address_page = cart_page.continue_to_checkout()
    address_page.fill_address_form(FIRST_NAME, LAST_NAME, ZIP_CODE)
    overview_page = address_page.proceed_to_overview_page()

    success_page = overview_page.finish_order()
    message = success_page.get_message()
    assert message == "Thank you for your order!"