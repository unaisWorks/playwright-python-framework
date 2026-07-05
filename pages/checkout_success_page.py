class CheckoutSuccessPage:
    #Locators
    TITLE = '[data-test="title"]'
    MESSAGE = '[data-test="complete-header"]'

    def __init__(self, page):
        self.page = page

    def get_title(self):
        return self.page.locator(self.TITLE).text_content()

    def get_message(self):
        return self.page.locator(self.MESSAGE).text_content()

