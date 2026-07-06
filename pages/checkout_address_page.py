class CheckoutAddressPage:
    #Locators
    TITLE =  '[data-test="title"]'
    FIRST_NAME_LOCATOR = '[data-test="firstName"]'
    LAST_NAME_LOCATOR = '[data-test="lastName"]'
    ZIP_CODE_LOCATOR = '[data-test="postalCode"]'
    CANCEL_BUTTON = '[data-test="cancel"]'
    CONTINUE_BUTTON = '[data-test="continue"]'

    def __init__(self, page):
        self.page = page

    def get_title(self):
        return self.page.locator(self.TITLE)

    def fill_address_form(self, first_name, last_name, zip_code):
        self.page.locator(self.FIRST_NAME_LOCATOR).fill(first_name)
        self.page.locator(self.LAST_NAME_LOCATOR).fill(last_name)
        self.page.locator(self.ZIP_CODE_LOCATOR).fill(zip_code)

    def proceed_to_overview_page(self):
        self.page.locator(self.CONTINUE_BUTTON).click()
        from pages.checkout_overview_page import CheckoutOverviewPage
        return CheckoutOverviewPage(self.page)