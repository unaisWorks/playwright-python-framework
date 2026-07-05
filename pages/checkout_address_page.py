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

    def fill_address_form(self, FIRST_NAME,LAST_NAME,ZIP_CODE):
       self.page.locator(self.FIRST_NAME_LOCATOR).fill(FIRST_NAME)
       self.page.locator(self.LAST_NAME_LOCATOR).fill(LAST_NAME)
       self.page.locator(self.ZIP_CODE_LOCATOR).fill(ZIP_CODE)

    def proceed_to_overview_page(self):
        self.page.locator(self.CONTINUE_BUTTON).click()
        from pages.checkout_overview_page import CheckoutOverviewPage
        return CheckoutOverviewPage(self.page)