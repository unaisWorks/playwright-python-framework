from pages.cart_page import CartPage
from pages.checkout_address_page import CheckoutAddressPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from data.address import FIRST_NAME,LAST_NAME,ZIP_CODE

username = "standard_user"
password = "secret_sauce"

def test_title(page):
    login_page = LoginPage(page)
    login_page.open()
    inventory_page = login_page.login(username, password)
    inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()
    address_page = cart_page.continue_to_checkout()
    title = address_page.get_title()

    assert title == "Checkout: Your Information"

def test_address_flow(page):
    login_page = LoginPage(page)
    login_page.open()
    inventory_page = login_page.login(username, password)
    inventory_page.add_to_cart()
    cart_page = inventory_page.click_cart_icon()
    address_page = cart_page.continue_to_checkout()
    address_page.fill_address_form(FIRST_NAME , LAST_NAME , ZIP_CODE)
    overview_page = address_page.proceed_to_overview_page()
    page_title = overview_page.get_title()

    assert page_title == "Checkout: Overview"


