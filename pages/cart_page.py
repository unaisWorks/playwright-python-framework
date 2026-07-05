from pages.checkout_address_page import CheckoutAddressPage


class CartPage:
    def __init__(self, page):
        self.page = page
    #Locators
    PAGE_TITLE = '[data-test="title"]'
    CONTINUE_SHOPPING_BUTTON = '[data-test="continue-shopping"]'
    CART_ITEM = '[data-test="inventory-item-name"]'
    ITEM_NAME = ".inventory_item_name"
    REMOVE_ITEM_BUTTON = '[id^="remove-"]'
    CHECKOUT = '[data-test="checkout"]'


    def get_page_title(self):
        return self.page.locator(self.PAGE_TITLE)

    def get_added_item_name(self):
        return self.page.locator(self.CART_ITEM).text_content().strip()

    def remove_item_from_cart(self):
        self.page.locator(self.REMOVE_ITEM_BUTTON).first.click()

    def continue_shopping(self):
        self.page.locator(self.CONTINUE_SHOPPING_BUTTON).click()
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.page)

    def get_added_item(self):
        return self.page.locator(self.CART_ITEM).text_content()

    def is_cart_empty(self):
        elements = self.page.locator(self.CART_ITEM)
        return elements.count() == 0

    def continue_to_checkout(self):
        self.page.locator(self.CHECKOUT).click()
        return CheckoutAddressPage(self.page)


