class CheckoutOverviewPage:
    TITLE = '[data-test="title"]'
    PRODUCT = '[data-test="inventory-item-name"]'
    CANCEL_BUTTON = '[data-test="cancel"]'
    FINISH_BUTTON = '[data-test="finish"]'


    def __init__(self, page):
        self.page = page

    def get_title(self):
        return self.page.locator(self.TITLE).text_content()

    def fetch_products_name(self):
        return self.page.locator(self.PRODUCT).text_content()

    def cancel_order(self):
        self.page.locator(self.CANCEL_BUTTON).click()
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.page)

    def finish_order(self):
        self.page.locator(self.FINISH_BUTTON).click()
        from pages.checkout_success_page import CheckoutSuccessPage
        return CheckoutSuccessPage(self.page)