from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

username = "standard_user"
password = "secret_sauce"

def test_inventory_page_title(page):
    login_page = LoginPage(page)
    login_page.open()
    inventory_page = login_page.login(username,password)
    inventory_title = inventory_page.get_page_title()
    print(inventory_title)
    assert "Swag Labs" in inventory_title

def test_inventory_page_url(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username,password)
    page_url = page.url

    assert "inventory" in page_url

def test_page_heading(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)
    inventory_page = InventoryPage(page)
    heading = inventory_page.get_inventory_page_heading()

    assert "Products" == heading

def test_add_to_cart_button(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)
    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart()
    button_text = inventory_page.get_remove_button_text()

    assert button_text == "Remove"

def test_remove_button(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)
    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart()
    inventory_page.remove_from_cart()
    button_text = inventory_page.get_add_button_text()

    assert button_text == "Add to cart"

def test_cart_icon_badge(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)
    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart()
    cart_count = inventory_page.get_cart_count()

    assert cart_count == "1"

def test_logout(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)
    inventory_page = InventoryPage(page)
    inventory_page.open_menu()
    inventory_page.logout_account()

    assert "Swag Labs" == page.title()

def test_sort_products_by_price_low_to_high(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)
    inventory_page = InventoryPage(page)
    inventory_page.sort_products("lohi")
    product_prices = inventory_page.get_product_prices()

    assert product_prices == sorted(product_prices)

def test_sort_products_by_price_high_to_low(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)
    inventory_page = InventoryPage(page)
    inventory_page.sort_products("hilo")
    product_prices = inventory_page.get_product_prices()

    assert product_prices == sorted(product_prices,reverse=True)

def test_sort_products_by_name_A_Z(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)
    inventory_page = InventoryPage(page)
    inventory_page.sort_products("az")
    product_names = inventory_page.get_product_names()

    assert product_names == sorted(product_names)

def test_sort_products_by_name_Z_A(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)
    inventory_page = InventoryPage(page)
    inventory_page.sort_products("za")
    product_names = inventory_page.get_product_names()

    assert product_names == sorted(product_names, reverse=True)