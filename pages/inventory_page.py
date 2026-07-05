class InventoryPage:
    #locators
    ADD_TO_CART_BUTTON = '[data-test="add-to-cart-sauce-labs-backpack"]'
    REMOVE_FROM_CART_BUTTON = '[data-test="remove-sauce-labs-backpack"]'
    CART_ICON = '[data-test="shopping-cart-link"]'
    CART_COUNT_BADGE = '[data-test="shopping-cart-badge"]'
    MENU_ICON = '#react-burger-menu-btn'
    LOGOUT_LINK = '[data-test="logout-sidebar-link"]'
    SORT_DROPDOWN = '[data-test="product-sort-container"]'
    PRODUCT_PRICES = '[data-test="inventory-item-price"]'
    PRODUCT_NAMES = '[data-test="inventory-item-name"]'
    HEADING = '[data-test="title"]'

    def __init__(self, page):
        self.page = page

    def get_page_title(self):
        return self.page.title()

    def add_to_cart(self):
        item_name = self.page.locator(self.PRODUCT_NAMES).first.text_content()
        self.page.locator(self.ADD_TO_CART_BUTTON).click()
        return item_name

    def get_add_button_text(self):
       return self.page.locator(self.ADD_TO_CART_BUTTON).text_content()

    def remove_from_cart(self):
        self.page.locator(self.REMOVE_FROM_CART_BUTTON).click()

    def get_remove_button_text(self):
        return self.page.locator(self.REMOVE_FROM_CART_BUTTON).text_content()

    def remove_item_from_cart(self):
        self.page.locator(self.REMOVE_FROM_CART_BUTTON).click()

    def get_cart_count(self):
        return self.page.locator(self.CART_ICON).text_content()

    def click_cart_icon(self):
        self.page.locator(self.CART_ICON).click()
        from pages.cart_page import CartPage
        return CartPage(self.page)

    def get_inventory_page_heading(self):
        return self.page.locator(self.HEADING).text_content()

    def open_menu(self):
        self.page.locator(self.MENU_ICON).click()

    def logout_account(self):
        return self.page.locator(self.LOGOUT_LINK).click()

    def sort_products(self,sort_option):
        dropdown = (self.page.locator(self.SORT_DROPDOWN))
        dropdown.select_option(sort_option)

    def get_product_prices(self):
        prices = self.page.locator(self.PRODUCT_PRICES).all_text_contents()
        return [float(
            price.replace("$","")
        )
            for price in prices
        ]

    def get_product_names(self):
        prices = self.page.locator(self.PRODUCT_NAMES).all_text_contents()
        return [price for price in prices]


