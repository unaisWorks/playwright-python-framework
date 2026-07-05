from pages.login_page import LoginPage
from data.address import FIRST_NAME, LAST_NAME, ZIP_CODE

username = "standard_user"
password = "secret_sauce"

def test_title_of_page(page):
    login_page = LoginPage(page)
    login_page.open()
    inventory_page = login_page.login(username,password)
    inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()
    address_page = cart_page.continue_to_checkout()
    address_page.fill_address_form(FIRST_NAME , LAST_NAME , ZIP_CODE)
    overview_page  = address_page.proceed_to_overview_page()

    title = overview_page.get_title()

    assert title ==  "Checkout: Overview"

def test_confirm_product_data(page):
    login_page = LoginPage(page)
    login_page.open()
    inventory_page = login_page.login(username, password)
    inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()
    added_product = cart_page.get_added_item()
    address_page = cart_page.continue_to_checkout()
    address_page.fill_address_form(FIRST_NAME, LAST_NAME, ZIP_CODE)
    overview_page = address_page.proceed_to_overview_page()
    products = overview_page.fetch_products_name()

    assert products == added_product

def test_cancel_order(page):
    login_page = LoginPage(page)
    login_page.open()
    inventory_page = login_page.login(username, password)
    inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()
    address_page = cart_page.continue_to_checkout()
    address_page.fill_address_form(FIRST_NAME, LAST_NAME, ZIP_CODE)
    overview_page = address_page.proceed_to_overview_page()
    inventory_page = overview_page.cancel_order()
    title = inventory_page.get_page_title()
    assert title == "Swag Labs"

def test_finish_order(page):
    login_page = LoginPage(page)
    login_page.open()
    inventory_page = login_page.login(username, password)
    inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()
    address_page = cart_page.continue_to_checkout()
    address_page.fill_address_form(FIRST_NAME, LAST_NAME, ZIP_CODE)
    overview_page = address_page.proceed_to_overview_page()
    success_page = overview_page.finish_order()
    title = success_page.get_title()

    assert title == "Checkout: Complete!"


